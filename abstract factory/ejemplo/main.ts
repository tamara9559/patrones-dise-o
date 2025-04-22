// 1. Interfaces de Chair y Sofa
interface Chair {
  assemble(): void;
}

interface Sofa {
  recline(): void;
}

// 2. Clases Concretas de muebles

class ModernChair implements Chair {
  assemble(): void {
    console.log('Assembling modern chair');
  }
}

class VictorianChair implements Chair {
  assemble(): void {
    console.log('Assembling victorian chair');
  }
}

class ModernSofa implements Sofa {
  recline(): void {
    console.log('Reclining modern sofa');
  }
}

class VictorianSofa implements Sofa {
  recline(): void {
    console.log('Reclining victorian sofa');
  }
}

// 3. Interfaz de la Fábrica Abstracta

interface FurnitureFactory {
  createChair(): Chair;
  createSofa(): Sofa;
}

// 4. Clases Concretas de Fábricas
class ModernFurnitureFactory implements FurnitureFactory {
  createChair(): Chair {
    return new ModernChair();
  }

  createSofa(): Sofa {
    return new ModernSofa();
  }
}

class VictorianFurnitureFactory implements FurnitureFactory {
  createChair(): Chair {
    return new VictorianChair();
  }
  createSofa(): Sofa {
    return new VictorianSofa();
  }
}

// 5. Código Cliente

function main(factory: FurnitureFactory) {
  const chair = factory.createChair();
  const sofa = factory.createSofa();

  chair.assemble();
  sofa.recline();
}

// Pruebas
console.log('Creating modern furniture:');
main(new ModernFurnitureFactory());

console.log('\nCreating victorian furniture:');
main(new VictorianFurnitureFactory());