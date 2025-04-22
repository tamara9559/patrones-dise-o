// 2. Clases Concretas de muebles
var ModernChair = /** @class */ (function () {
    function ModernChair() {
    }
    ModernChair.prototype.assemble = function () {
        console.log('Assembling modern chair');
    };
    return ModernChair;
}());
var VictorianChair = /** @class */ (function () {
    function VictorianChair() {
    }
    VictorianChair.prototype.assemble = function () {
        console.log('Assembling victorian chair');
    };
    return VictorianChair;
}());
var ModernSofa = /** @class */ (function () {
    function ModernSofa() {
    }
    ModernSofa.prototype.recline = function () {
        console.log('Reclining modern sofa');
    };
    return ModernSofa;
}());
var VictorianSofa = /** @class */ (function () {
    function VictorianSofa() {
    }
    VictorianSofa.prototype.recline = function () {
        console.log('Reclining victorian sofa');
    };
    return VictorianSofa;
}());
// 4. Clases Concretas de Fábricas
var ModernFurnitureFactory = /** @class */ (function () {
    function ModernFurnitureFactory() {
    }
    ModernFurnitureFactory.prototype.createChair = function () {
        return new ModernChair();
    };
    ModernFurnitureFactory.prototype.createSofa = function () {
        return new ModernSofa();
    };
    return ModernFurnitureFactory;
}());
var VictorianFurnitureFactory = /** @class */ (function () {
    function VictorianFurnitureFactory() {
    }
    VictorianFurnitureFactory.prototype.createChair = function () {
        return new VictorianChair();
    };
    VictorianFurnitureFactory.prototype.createSofa = function () {
        return new VictorianSofa();
    };
    return VictorianFurnitureFactory;
}());
// 5. Código Cliente
function main(factory) {
    var chair = factory.createChair();
    var sofa = factory.createSofa();
    chair.assemble();
    sofa.recline();
}
// Pruebas
console.log('Creating modern furniture:');
main(new ModernFurnitureFactory());
console.log('\nCreating victorian furniture:');
main(new VictorianFurnitureFactory());
