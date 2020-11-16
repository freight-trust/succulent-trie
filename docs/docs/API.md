# Documentation

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
const proxima = require("proxima-db");
const { BLAKE2b, randomBytes } = bcrypto;
const { Tree, Proof } = proxima;
```

:::

::::

## Basic Operations

#### Create

| name   | type   | description          |
| ------ | ------ | -------------------- |
| table  | string | name of the table    |
| schema | JSON   | schema for the table |

This creates a table with name, tableName, and returns a confirmation boolean if correct.

:::: tabs

::: tab javascript

```javascript
let table = "transactions"
let schema = {
  balance: 'uint'
  account: 'string'
}
var transactions = proxima.create(table, schema)
```

:::

::::

## Closing the database

| name  | type   | description       |
| ----- | ------ | ----------------- |
| table | string | name of the table |

:::: tabs

::: tab javascript

```javascript
await proxima.close(table);
```

:::

::::

#### Put

| name      | type        | description                     |
| --------- | ----------- | ------------------------------- |
| tableName | string      | name of the table               |
| key       | byte array  | key for the value               |
| value     | bytes array | value being placed in the table |

This operation does a put, and returns a proof.

:::: tabs

::: tab javascript

```javascript
let key = ".....";
let value = {
	account: key,
	value: 1000,
};
proxima.put(transactions, key, value);
```

:::

::::

#### Get

| name  | type       | description       |
| ----- | ---------- | ----------------- |
| table | string     | name of the table |
| key   | byte array | key for the value |

Gets a value corresponding to the key, within the tableName.

:::: tabs

::: tab javascript

```javascript
proxima.get(transactions, key);
```

:::

::::

#### Remove

| name      | type       | description       |
| --------- | ---------- | ----------------- |
| tableName | string     | name of the table |
| key       | byte array | key for the value |

Deletes the value associated with the key at the designated table.

### Verification

### Verification

:::: tabs

::: tab javascript

```javascript
const [code, value] = proof.verify(root, key, BLAKE2b, 256);
```

:::

::::

## Filters, Aggregates, Maps, and Groups

### Filter

Each filter can be shown as a combination of three variables.

| name       | type                        | description                |
| ---------- | --------------------------- | -------------------------- |
| name       | string                      | name of the table          |
| expression | string                      | key for the predicate type |
| value      | integer, string, value type | key for the value          |

:::: tabs

::: tab javascript

```javascript
let filter = [
	{
		name: "name",
		expression: "=",
		value: "hello",
	},
];
proxima.filter(transactions, filter);
```

:::

::::

## Batching Operations

### Checking out

:::: tabs

::: tab javascript

```javascript
const txn = tree.transaction();
```

:::

::::

### Adding values

:::: tabs

::: tab javascript

```javascript
await txn.insert(k, v);
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

### Committing

:::: tabs

::: tab javascript

```javascript
const root = await txn.commit();
```

:::

::::

### Getting snapshot

:::: tabs

::: tab javascript

```javascript
const root = await txn.commit();
const snapshot = tree.snapshot(root);
```

:::

::::
