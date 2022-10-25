# Stocks

![Splash](docs/splash.jpg)

## Introduction

Builds a database containing historical financial data for components of the S&P 600, 500 & 400 indexes.  This database
is provided for educational and private use, it should not be relied upon in any why to support the making of 
investment decisions.  **The provider accepts no responsibility whatsoever for its accuracy or suitability for purpose,
so use and abuse at your own risk.**

## Entity Model

![Entity Model](docs/database.png)

The database has many supporting tables whose names begin with z_ or zs_ and are not documented here as they are only
used to build the final tables.

In addition to this there are a series of audit tables used to track changes to the main tables.  These tables names
begin with xxx_ and are not documented here either as they are primarily intended for debugging and tracking.