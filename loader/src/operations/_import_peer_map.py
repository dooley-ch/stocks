# *******************************************************************************************
#  File:  _import_peer_map.py
#
#  Created: 27-10-2022
#
#  History:
#  27-10-2022: Initial version
#
# *******************************************************************************************

__author__ = "James Dooley"
__contact__ = "james@developernotes.org"
__copyright__ = "Copyright (c) 2022 James Dooley <james@dooley.ch>"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "James Dooley"
__status__ = "Production"

__all__ = ['import_peers_file']

import related
from loguru import logger
from rich.progress import Progress, TaskID

from .. import config
from .. import datastore as ds
from .. import model


@related.immutable
class _PeerMap:
    """
    This class represents a record in the peers.json file
    """
    ticker: str = related.StringField(required=True)
    name: str = related.StringField(required=True)
    peers: list[str] = related.SequenceField(cls=str, default=list())


@related.immutable
class _PeerMapFile:
    """
    This class represents the contents of the peers.json file
    """
    entries: list[_PeerMap] = related.SequenceField(cls=_PeerMap, default=list())


@logger.catch(reraise=True)
def import_peers_file(progress: Progress, task: TaskID) -> bool:
    """
    This function imports the peers file
    """
    estimated_rows = 8_800
    actual_rows = 0
    processed_rows = 0

    progress.update(task, visible=True, total=estimated_rows)

    file = config.data_folder().joinpath(config.PEERS_FILE)
    if not file.exists():
        raise ValueError(f"Can't find Peers file: {file}")

    with file.open('r') as f:
        contents = f.read()

    data = related.from_json(contents, _PeerMapFile)

    db_conn = ds.get_connection(config.database_info())

    with db_conn.cursor() as cursor:
        # noinspection SqlWithoutWhere
        cursor.execute("DELETE FROM z_peer_map;")

    with db_conn:
        for entry in data.entries:
            processed_rows += 1

            ticker = entry.ticker
            for peer in entry.peers:
                record = model.zPeerMapRecord(ticker=ticker, peer=peer)
                ds.zPeerMapRecord_insert(record, db_conn)

            actual_rows += 1
            if actual_rows < estimated_rows:
                progress.update(task, advance=1)

    progress.update(task, completed=estimated_rows)

    logger.info(f"Imported Peer Map file: Actual Rows - {actual_rows}, Inserted Rows - {processed_rows}")

    return True
