### Настройка проекта CDK — решение

### Упражнение

Инициализируйте проект CDK и настройте файлы, необходимые для сборки проекта CDK.

### Решение

#### Инициализация проекта CDK

1. Установите CDK на свой компьютер, запустив `npm install -g aws-cdk`.
2. Создайте новый каталог с именем «sample» для вашего проекта и запустите «cdk init app --language typescript», чтобы инициализировать проект CDK. Вы можете выбрать язык: csharp, fsharp, go, java, javascript, python или typescript.
3. Вы увидите следующие файлы, созданные в вашем каталоге:
   1. `cdk.json`, `tsconfig.json`, `package.json` — это файлы конфигурации, которые используются для определения некоторых глобальных настроек вашего проекта CDK.
   2. `bin/sample.ts` — это точка входа для вашего проекта CDK. Этот файл используется для определения стека, который вы хотите создать.
   3. `lib/sample-stack.ts` — это основной файл, который будет содержать код вашего проекта CDK.

#### Создайте образец лямбда-функции

1. В файл lib/sample-stack.ts добавьте следующий код для создания лямбда-функции:

```typescript
import * as cdk from 'aws-cdk-lib';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import { Construct } from 'constructs';

export class SampleStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const hello = new lambda.Function(this, 'SampleLambda', {
      runtime: lambda.Runtime.NODEJS_14_X,
      code: lambda.Code.fromInline('exports.handler = async () => "hello world";'),
      handler: 'index.handler'
    });
  }
}

Это создаст образец лямбда-функции, которая при вызове возвращает «hello world».

#### Запускаем проект CDK

Прежде чем развернуть проект. Вам необходимо запустить свой проект. Это создаст стек CloudFormation, который будет использоваться для развертывания вашего проекта. Вы можете загрузить свой проект, запустив `cdk bootstrap`.

Узнайте больше о начальной загрузке [здесь](https://docs.aws.amazon.com/cdk/latest/guide/bootstrapping.html).

##### Развертывание проекта

1. Запускайте npm install, чтобы устанавливать все зависимости вашего проекта всякий раз, когда вы вносите изменения.
2. Запустите `cdk Synth`, чтобы синтезировать шаблон CloudFormation для вашего проекта. Вы увидите новый файл cdk.out/CDKToolkit.template.json, который содержит шаблон CloudFormation для вашего проекта.
3. Запустите «cdk diff», чтобы увидеть изменения, которые будут внесены в вашу учетную запись AWS. Вы увидите новый стек под названием SampleStack, который создаст лямбда-функцию и все связанные с ней изменения.
4. Запустите `cdk Deploy`, чтобы развернуть проект. Вы должны увидеть новый стек под названием «Созданный» в вашей учетной записи AWS в разделе CloudFormation.
5. Перейдите в консоль Lambda, и вы увидите новую лямбда-функцию под названием SampleLambda, созданную в вашей учетной записи.