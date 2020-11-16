#  Registry

The  Registry is designed to interact with the chain, and the registry.

## Installation

`npm install`

## Use

`node index.js`

## API

### Get Registry Address

```javascript
registry.getRegistryAddress();
```

This function returns the address of the registry.

### Get Services

```javascript
var services = registry.getServices();
```

This function returns the list of services by ID.

### Get Service

```javascript
var serviceId = services[0];
registry.getService(serviceId);
```

| name      | type    | description       |
| --------- | ------- | ----------------- |
| serviceId | uint256 | id of the service |

This returns the associated service variables.

### Get Bootstraps

```javascript
var serviceId = services[0];
registry.getBootstraps(serviceId);
```

| name      | type    | description       |
| --------- | ------- | ----------------- |
| serviceId | uint256 | id of the service |

This returns the associated bootstrap nodes with the service.

## Schema

### Service

```javascript
    struct Service {
        uint256 serviceId;
        string id;
        address owner;
        uint256 index;
        string name;
        bytes32[] bootstraps;
        uint256 stake;

    }
```
