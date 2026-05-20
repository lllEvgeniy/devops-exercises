## Перл

### Самооценка Perl

<details>
<summary>Что такое Перл?</summary><br><b>

Из официальной [документации](https://perldoc.perl.org/):

«Perl официально означает «Практическое извлечение и язык отчетов», за исключением случаев, когда это не так».

Это язык программирования общего назначения, разработанный в основном для работы с текстом. Он использовался для выполнения задач системного администрирования, работы в сети, создания веб-сайтов и многого другого.

</b></details>

<details>
<summary>Какие типы данных есть в Perl? И как мы можем это определить?</summary><br><b>

- Скаляр: это простая переменная, в которой хранятся отдельные элементы данных. Это может быть строка, число или ссылка.

```
my $number = 5;
```

- Массивы: это список скаляров.

```
my @numbers = (1, 2, 3, 4, 5);
# или через ключевое слово `qw` (quote word):
my @numbers = qw/1 2 3 4 5/;
# вместо `/` можно использовать другой разделитель, например qw@1 2 3 4 5@
```

- Хэши (или ассоциативные массивы): это неупорядоченная коллекция пар ключ-значение. Мы можем получить доступ к хешу, используя ключи.

```
my %numbers = (
  First => '1',
  Second => '2',
  Third => '3'
);
```

</b></details>

<details>
<summary>Как получить доступ к хэш-значению, добавить и удалить пару ключ/значение и изменить хэш?</summary><br><b>

```
my %numbers = (
  'First' => '1',
  'Second' => '2',
  'Third' => '3'
);
```

- Доступ:

```
print($numbers{'First'});
```

- Добавить:

```
$numbers{'Fourth'} = 4;
```

- Удалить:

```
delete $numbers{'Third'};
```

- Изменить:

```
$numbers{'Fifth'} = 6;
$numbers{'Fifth'} = 5;
```

</b></details>

<details>
<summary>Как можно перебрать массив? А хеш?</summary><br><b>

- Массив:

```
my @numbers = qw/1 2 3 4 5/;

# `$_` — текущий элемент итерации; цикл от первого индекса до последнего
foreach (@numbers) {
    print($_);
}
# Вывод: 12345

# `$#array` — максимальный индекс массива; итерация от 0 до этого индекса
for my $i (0..$#numbers) {
    print($numbers[$i]);
}
# Вывод: 12345

# Через `map`:
print map {$_} @numbers;
# Вывод: 12345

# Через `while`. Осторожно: `shift` удаляет первый элемент массива
# и возвращает его; после цикла массив `@numbers` может оказаться пустым
while (my $element = shift(@numbers)) {
    print($element);
}
# Вывод: 12345
```

- Хэши:

```
my %capital_cities = (
  'Madrid' => 'Spain',
  'Rome' => 'Italy',
  'Berlin' => 'Germany'
);

# Перебор ключей:
foreach my $city (keys %capital_cities) {
    print($city . "\n");
}

# Перебор значений:
foreach my $country (values %capital_cities) {
    print($country . "\n");
}

# Ключи и значения (через keys):
foreach my $city (keys %capital_cities) {
    print("Город: $city — страна: $capital_cities{$city}\n");
}

# Ключи и значения (через each):
while (my ($city, $country) = each %capital_cities) {
    print("Город: $city — страна: $country\n");
}
```

</b></details>

<details>
<summary>Что такое подпрограмма Perl? Как это определить?</summary><br><b>

Это модель Perl для пользовательских функций (она также называется функцией, как и в других языках программирования). Мы можем определить подпрограмму с помощью ключевого слова `sub`.

```
sub hello {
  print "hello";
}
```

</b></details>

<details>
<summary>Описать различные способы получения параметров в подпрограмме.</summary><br><b>

- Назначение списка: использование массива `@_`. Это список элементов, которые передаются в качестве параметров.

```
sub power {
    my ($b, $e) = @_;
    return $b ** $e;
}

&power(2, 3);
```

- Индивидуальное назначение: мы должны получить доступ к каждому элементу массива `@_`. Он начинается с нуля.

```
sub power {
    my $b = $_[0];
    my $e = $_[1];
    return $b ** $e;
}

&power(2, 3);
```

- Использование ключевого слова `shift`: оно используется для удаления первого значения массива и его возврата.

```
sub power {
    my $b = shift;
    my $e = shift;
    return $b ** $e;
}

&power(2, 3);
```

Подробнее — в [ответе на Stack Overflow](https://stackoverflow.com/a/21465275/12771230).

</b></details>

<details>
<summary>Что такое лексическая и динамическая область видимости?</summary><br><b>

**Лексическая (статическая)** — видимость по месту объявления в коде (`my $x` в блоке).<br>
**Динамическая** — по цепочке вызовов (`local`, старый `use vars`); в Perl по умолчанию лексическая через `my`; `local` временно подменяет глобальную переменную в динамической области видимости.

</b></details>

<details>
<summary>Как применять ссылки и разыменования?</summary><br><b>

Ссылка: `\$scalar`, `\@array`, `\%hash`. Разыменование: `${$ref}`, `@{$aref}`, `%{$href}`. Передача по ссылке в подпрограмму изменяет оригинал; для ссылки на массив: `push @$aref, $val`.

</b></details>

<details>
<summary>Есть ли в Perl соглашения?</summary><br><b>

Вы можете проверить [perlstyle](https://perldoc.perl.org/perlstyle)

</b></details>

<details>
<summary>Что такое Perl POD? Можете ли вы закодировать пример?</summary><br><b>

Из официальной [документации](https://perldoc.perl.org/perlpod):

«Pod — это простой в использовании язык разметки, используемый для написания документации для Perl, программ Perl и модулей Perl».

```
=item
    Возвращает факториал числа.
    Вход: $n (число для вычисления).
    Выход: факториал числа.
=cut
sub factorial {
    my ($i, $result, $n) = (1, 1, shift);
    $result = $result *= $i && $i++ while $i <= $n;
    return $result;
}
```

</b></details>

### Регулярное выражение Perl

<details>
<summary>Проверьте, существует ли в строке слово «электроэнцефалографист».</summary><br><b>

```
my $string = "The longest accepted word by RAE is: electroencefalografista";
if ($string =~ /electroencefalografista/) {
    print "Совпадение!\n";
}
```

</b></details>

<details>
<summary>Проверьте, не существует ли в строке слова «электроэнцефалографист».</summary><br><b>

```
my $string = "The longest not accepted word by RAE is: Ciclopentanoperhidrofenantreno";
if ($string !~ /electroencefalografista/) {
    print "Нет совпадения!\n";
}
```

</b></details>


<details>
<summary>Замените слово «удивительно».</summary><br><b>

```
my $string = "Perl is amazing!";
$string =~ s/amazing/incredible/;  # замена подстроки amazing → incredible
print $string;
# Вывод: Perl is incredible!
```

</b></details>

<details>
<summary>Извлеките `hh:mm:ss` с захватом группы `()` в следующую дату и время.</summary><br><b>

```
my $date = "Fri Nov 19 20:09:37 CET 2021";
my @matches = $date =~ /(.*)(\d{2}:\d{2}:\d{2})(.*)/;
print $matches[1];
# Вывод: 20:09:37
```

</b></details>

<details>
<summary>Извлеките все элементы, которые являются числами в массиве</summary><br><b>

```
my @array = ('a', 1, 'b', 2, 'c', 3);
my @numbers = grep (/\d/, @array);    # Примечание: \d — не только цифры 0-9
map { print $_ . "\n" } @numbers;
```

</b></details>

<details>
<summary>Выведите всех пользователей системы Linux, имена которых начинаются с d или D.</summary><br><b>

- С однострочным Perl:

```
open(my $fh, '<', '/etc/passwd');
my @user_info = <$fh>;
map { print $& . "\n" if $_ =~ /^d([^:]*)/ } @user_info;
close $fh;
```

- Без однострочника:

```
foreach my $user_line (@user_info) {
    if ($user_line =~ /^d([^:]*)/) {
        print $& . "\n";
    }
}
```

</b></details>

### Дескриптор файлов Perl

<details>
<summary>Упомяните различные режимы работы с файлами.</summary><br><b>

- Только чтение: `<`
- Режим записи. Он создает файл, если он не существует: `>`
- Режим добавления. Он создает файл, если он не существует: `>>`
- Режим чтения и записи: `+<`
- Режим чтения, очистки и записи. Он создает файл, если он не существует: `+>`
- Прочитай и дополни. Он создает файл, если он не существует: `+>>`

</b></details>

<details>
<summary>Как записать в файл?</summary><br><b>

```
# Режимы:
# '>'  — запись (очищает файл, если он уже существует)
# '>>' — дозапись в конец
open(my $fh, '>>', 'file_name.ext') or die "Ошибка: не удалось открыть файл";
print $fh "текст для записи...\n";
close($fh);
```

</b></details>

<details>
<summary>Как можно прочитать файл и распечатать каждую строку?</summary><br><b>

```
open(my $fh, '<', 'file_to_read.ext') or die "Ошибка: не удалось открыть файл";
my @file = <$fh>;
foreach my $line (@file) {
    print $line;
}
```

Мы можем использовать дескриптор файла, не присваивая его массиву:

```
open(my $fh, '<', 'file_to_read.ext') or die "Ошибка: не удалось открыть файл";

foreach my $line (<$fh>) {
    print $line;
}
```

</b></details>

### Перл ООП

<details>
<summary>Есть ли в Perl поддержка ООП?</summary><br><b>

Из официальной [документации](https://perldoc.perl.org/perlootut):

«По умолчанию встроенная объектно-ориентированная система Perl очень минималистична, поэтому большую часть работы остается выполнять вам».

</b></details>

<details>
<summary>Какова цель функции `bless`?</summary><br><b>

Функция `bless` используется для превращения простой структуры данных в объект.

</b></details>

<details>
<summary>Как создать класс Perl? Как можно вызвать метод?</summary><br><b>

- Создадим пакет: `Example.pm`

```
package Example;

sub new {
    my $class = shift;
    my $self = {};
    bless $self, $class;
    return $self;
}

sub is_working {
    print "Работает!\n";
}

1;
```

- Теперь мы можем создать экземпляр класса `Example` и вызвать метод `is_working`:

```
my $e = new Example();
$e->is_working();
# Вывод: Работает!
```

</b></details>

<details>
<summary>Есть ли в Perl наследование? Что такое ключевое слово `SUPER`?</summary><br><b>

Да, Perl поддерживает наследование. Об этом можно прочитать в официальной [документации](https://perldoc.perl.org/perlobj#Inheritance).
Мы также можем прочитать о ключевом слове `SUPER`, которое используется для вызова метода родительского класса. Это пример того, как мы можем применять наследование.

</b></details>

<details>
<summary>Есть ли в Perl полиморфизм? Что такое переопределение метода?</summary><br><b>

Да, у него есть полиморфизм. Фактически переопределение метода — это способ применить его в Perl.

Переопределение метода простыми словами появляется, когда у нас есть класс с методом, который уже существует в родительском классе.

Пример:

```
package A;

sub new { return bless {}, shift; };
sub printMethod { print "A\n"; };

package B;

use parent -norequire, 'A';

sub new { return bless {}, shift; };
sub printMethod { print "B\n"; };

my $a = A->new();
my $b = B->new();

A->new()->printMethod();
B->new()->printMethod();

# Вывод:
# A
# B
```

</b></details>

<details>
<summary>Как можно вызвать метод унаследованного класса?</summary><br><b>

```
# Класс `A` с методом `printA`
package A;

sub new { return bless {}, shift; };
sub printA { print "A"; };

# Класс `B`, наследующий `A`
package B;

use parent -norequire, 'A';

sub new { return bless {}, shift; };

# Экземпляр `B` может вызвать унаследованный метод
my $b = B->new();
$b->printA();
```

</b></details>

### Обработка исключений Perl

<details>
<summary>Как мы можем оценить и перехватить исключение в Perl?</summary><br><b>

Из официальной [документации по eval](https://perldoc.perl.org/functions/eval):

«`eval` во всех своих формах используется для выполнения небольшой программы Perl, перехватывая любые возникающие ошибки, чтобы они не привели к сбою вызывающей программы».

Например:

```
eval {
    die;
};
if ($@) {
    print "Ошибка. Подробности: $@";
}
```

Если мы выполним это, мы получим следующий вывод:

```
Ошибка. Подробности: Died at eval.pl line 2.
```

`eval` (аналог `try` в других языках) пытается выполнить код. Этот код завершается с ошибкой (`die`), затем условие `if` проверяет переменную `$@`, в которой сохранено сообщение об ошибке. Так в Perl обрабатывают исключения.

</b></details>

### Перл ОС

<details>
<summary>Что такое Perl Open3?</summary><br><b>

Из официальной документации [IPC::Open3](https://perldoc.perl.org/IPC::Open3):

«IPC::Open3 — открыть процесс чтения, записи и обработки ошибок с помощью open3()».

С помощью `open3` мы можем иметь полный контроль над STDIN, STDOUT, STDERR. Обычно он используется для выполнения команд.

</b></details>

<details>
<summary>Использование Open3: создайте файл размером 15 МБ и проверьте его успешное создание.</summary><br><b>

- Код:

```
use IPC::Open3;
use Data::Dumper;

sub execute_command {
    my @command_to_execute = @_;
    my ($stdin, $stdout, $stderr);
    eval {
        open3($stdin, $stdout, $stderr, @command_to_execute);
    };
    if ($@) {
        print "Ошибка. Подробности: $@";
    }
    close($stdin);
    return $stdout;
}

my $file_name = 'perl_open3_test';
&execute_command('truncate', '-s', '15M', $file_name);
my $result = &execute_command('stat', '-c', '%s', $file_name);
print Dumper(<$result>);
```

- Результат:

```
$ -> perl command.pl
$VAR1 = '15728640
';
```

</b></details>

### Пакеты и модули Perl

<details>
<summary>Что такое пакет Perl? А модуль?</summary><br><b>

С помощью пакета Perl мы определяем пространство имен.
Модуль Perl одним простым словом можно определить как «класс». Когда мы создаем класс в Perl, мы используем ключевое слово package. Модуль можно использовать с ключевым словом `use`.

</b></details>

<details>
<summary>В чем разница между расширениями .pl и .pm?</summary><br><b>

Между расширениями `.pm` и `.pl` нет реальной разницы. Perl использует расширения .pm только для того, чтобы отличить его от модуля Perl (класса). Расширения `.pl` обычно называются для Perl-скриптов без классов ООП.

</b></details>

<details>
<summary>Почему класс (или модуль) Perl должен возвращать что-то в конце файла? Проверьте пример.</summary><br><b>

Если мы хотим «использовать» модуль Perl («импортировать» класс), этот модуль должен заканчиваться значением, отличным от 0. Это необходимо, потому что если мы попытаемся импортировать класс и у него будет ложное значение, мы не сможем его использовать.

```
package A;

sub new { return bless {}, shift; };
sub printMethod { print "A\n"; };

1;
```

</b></details>

<details>
<summary>Что такое CPAN? А cpanm?</summary><br><b>

CPAN (Comprehensive Perl Archive Network) — комплексная сеть архивов Perl.

**cpanm**. Из официального [App::cpanminus](https://metacpan.org/pod/App::cpanminus):
«App::cpanminus — получение, распаковка, сборка и установка модулей из CPAN».

[Найти модули CPAN](https://metacpan.org/)

</b></details>

<details>
<summary>Как установить cpanm и модуль Perl?</summary><br><b>

Существует несколько различных альтернатив установке модулей Perl. Мы будем использовать cpanm.

- Установите `cpanm`:

```
$ cpan App::cpanminus
```

- Установите модуль Test с помощью cpanm:

```
cpanm Test
```

Теперь мы можем протестировать установленный модуль Test:

```
perl -M'Test::Simple tests => 1' -e 'ok( 1 + 1 == 2 );'
1..1
ok 1
```

```
$ perl -M'Test::Simple tests => 1' -e 'ok( 1 + 1 == 3 );'
1..1
not ok 1
#   Failed test at -e line 1.
# Looks like you failed 1 test of 1.   # сообщение Test::Simple (на английском)
```

</b></details>
