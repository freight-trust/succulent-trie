# Getting Started

::: warning

### _Currently under development_

:::

## Installation

:::: tabs

::: tab javascript

```javascript
npm install proxima-db
```

:::

::::

## Set-up

:::: tabs

::: tab javascript

```javascript
const bcrypto = require("bcrypto");
const Proxima = require("proxima-db");
var proxima = new Proxima();
```

:::

::::

## Creating a database

Creating a table for transactions

:::: tabs

::: tab javascript

```javascript
let table = "transactions";
let schema = {
	id: "string",
	from: "string",
	to: "string",
	amount: "uint",
};
var transactions = proxima.create(table, schema);
```

:::

::::

## Opening the database

:::: tabs

::: tab javascript

```javascript
await proxima.load(table);
```

:::

::::

## Adding values

Put key and value into db

:::: tabs

::: tab javascript

```javascript
let key = "id";
let transaction = {
	id: key,
	from: "address1",
	to: "address2",
	amount: 20000,
};
proxima.put(transactions, key, value);
```

:::

::::

## Getting value

Get item from the table

:::: tabs

::: tab javascript

```javascript
const proof, value = proxima.get(transactions, key)
```

:::

::::

### Verification

:::: tabs

::: tab javascript

```javascript
const [code, value] = proxima.verify(root, key, BLAKE2b, 256);
```

:::

::::

## Closing the database

:::: tabs

::: tab javascript

```javascript
await proxima.close();
```

:::

::::
