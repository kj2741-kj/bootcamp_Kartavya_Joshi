# 🥇 Zinc Arbitrage Trading System

A comprehensive Python-based system for analyzing and executing arbitrage opportunities between LME (London Metal Exchange) and MCX (Multi Commodity Exchange) zinc markets.

## 🎯 Overview

This system provides sophisticated analysis of zinc arbitrage opportunities, incorporating:
- **Live market data** from LME, MCX, and FX markets
- **Comprehensive cost analysis** including carry costs, freight, and transaction fees
- **Advanced decision engine** with multi-criteria scoring
- **Real-time monitoring** with automated alerts
- **Risk management** and position sizing recommendations
- **Monte Carlo simulation** and sensitivity analysis

## Features

### Core Analysis
- Real-time price data fetching from multiple sources
- Quality-adjusted price conversions (LME 99.995% vs MCX 99.5%)
- Comprehensive cost modeling (financing, storage, freight, transactions)
- Multi-currency support with live FX rates

### Decision Engine
- Multi-criteria opportunity evaluation
- Risk-adjusted return calculations
- Automated trade recommendations (STRONG BUY/BUY/HOLD)
- Position sizing using Kelly Criterion and risk management

### Risk Management
- Value-at-Risk (VaR) calculations
- Stress testing and scenario analysis
- Portfolio correlation monitoring
- Dynamic stop-loss and take-profit levels

### Monitoring & Alerts
- Real-time opportunity monitoring
- Configurable alert thresholds
- Email/SMS notification support
- Performance tracking and reporting


## 🔍 Data Sources

### Current Implementation
- **LME Data**: Simulated based on recent market prices
- **MCX Data**: Simulated based on recent market prices  
- **FX Data**: Yahoo Finance API (live USD/INR rates)
- **Freight**: Simulated based on typical shipping rates

