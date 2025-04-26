// 2. Productos concretos para la familia 1
var ConcreteProductA1 = /** @class */ (function () {
    function ConcreteProductA1() {
    }
    ConcreteProductA1.prototype.operationA = function () {
        console.log('Operation from ConcreteProductA1');
    };
    return ConcreteProductA1;
}());
var ConcreteProductB1 = /** @class */ (function () {
    function ConcreteProductB1() {
    }
    ConcreteProductB1.prototype.operationB = function () {
        console.log('Operation from ConcreteProductB1');
    };
    return ConcreteProductB1;
}());
// 3. Productos concretos para la familia 2
var ConcreteProductA2 = /** @class */ (function () {
    function ConcreteProductA2() {
    }
    ConcreteProductA2.prototype.operationA = function () {
        console.log('Operation from ConcreteProductA2');
    };
    return ConcreteProductA2;
}());
var ConcreteProductB2 = /** @class */ (function () {
    function ConcreteProductB2() {
    }
    ConcreteProductB2.prototype.operationB = function () {
        console.log('Operation from ConcreteProductB2');
    };
    return ConcreteProductB2;
}());
// 5. Fábrica concreta 1
var ConcreteFactory1 = /** @class */ (function () {
    function ConcreteFactory1() {
    }
    ConcreteFactory1.prototype.createProductA = function () {
        return new ConcreteProductA1();
    };
    ConcreteFactory1.prototype.createProductB = function () {
        return new ConcreteProductB1();
    };
    return ConcreteFactory1;
}());
// 6. Fábrica concreta 2
var ConcreteFactory2 = /** @class */ (function () {
    function ConcreteFactory2() {
    }
    ConcreteFactory2.prototype.createProductA = function () {
        return new ConcreteProductA2();
    };
    ConcreteFactory2.prototype.createProductB = function () {
        return new ConcreteProductB2();
    };
    return ConcreteFactory2;
}());
// 7. Código Cliente
var Client = /** @class */ (function () {
    function Client(factory) {
        this.productA = factory.createProductA();
        this.productB = factory.createProductB();
    }
    Client.prototype.someOperation = function () {
        this.productA.operationA();
        this.productB.operationB();
    };
    return Client;
}());
// 8. Pruebas
console.log('Using ConcreteFactory1:');
var client1 = new Client(new ConcreteFactory1());
client1.someOperation();
console.log('\nUsing ConcreteFactory2:');
var client2 = new Client(new ConcreteFactory2());
client2.someOperation();
