# Tutorial

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

## Step 0 Set-up

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

## Step 1: Creating a database

:::: tabs

::: tab javascript

```javascript
const tree = new Tree(BLAKE2b, 256, "/path/to/my/db");
```

:::

::::

## Step 2: Opening the database

:::: tabs

::: tab javascript

```javascript
await tree.open();
```

:::

::::

## Step 3: Checking out

:::: tabs

::: tab javascript

```javascript
const txn = tree.transaction();
```

:::

::::

## Step 4: Adding values

:::: tabs

::: tab javascript

```javascript
await txn.insert(k, v);
```

:::

::::

## Step 5: Committing

:::: tabs

::: tab javascript

```javascript
const root = await txn.commit();
```

:::

::::

## Step 6: Getting snapshot

:::: tabs

::: tab javascript

```javascript
const root = await txn.commit();
const snapshot = tree.snapshot(root);
```

:::

::::

## Step 7: Getting values

:::: tabs

::: tab javascript

```javascript
const value = await snapshot.get(key);
```

:::

::::

### Step 8: Proof of value

:::: tabs

::: tab javascript

```javascript
const proof = await snapshot.prove(key);
```

:::

::::

### Step 9: Verification

:::: tabs

::: tab javascript

```javascript
const [code, value] = proof.verify(root, key, BLAKE2b, 256);
```

:::

::::

## Step 10: Closing the database

:::: tabs

::: tab javascript

```javascript
await tree.close();
```

:::

::::
