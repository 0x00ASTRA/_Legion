# Creating an Economy

An economy system is the backbone of trade within a system. It enables users to trade items, currency, and information. Below is a map of how I designed the Economy for _Legion.

## Table of Contents:

### [Section 1]: **Design**

>[Architecture](#architecture)

### [Section 2]: **Objects**

>[Transactions](#transactions)
>[Items](#items)
>[Payment Accounts](#payment-accounts)
>[Payment Method](#payment-method)
>[Payment Handler](#payment-handler)

### [Section 3]: **Usage**

>[Creating a Transaction](#creating-a-transaction)
>[Adding an Item](#adding-an-item)
>[Creating a Payment Method](#creating-a-payment-method)
>[Creating an Account](#creating-an-account)
>[Handling Payments](#handling-payment)

---

## Design

### Architecture

```graphviz
diagraph economy {
    node [shape=box];
    Character;
    Marketplace;
    PaymentAccount;
    PaymentHandler;
    MarketplaceItem;
    
    Character -> PaymentAccount;
    Marketplace -> PaymentHandler;
    Marketplace -> MarketplaceItem;
}
```

---

## Objects

---

## Objects


---

## Usage