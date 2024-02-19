# Java Cheat Sheet

## Native

- Compile a .java file `javac <file_path>`
- Compile a project `javac -d <output_folder> -sourcepath <src_root_folder> <path_to_file_with_main>`
- Run a .class file `java <main>`

## Gradle

- Add a dependency to gradle in `build.gradle`

```gradle
dependencies {
    runtimeOnly(group = "org.springframework", name = "spring-core", version = "2.5")
}
```

- Clean application `gradle clean`
- Build application `gradle build`

## jUnit

- Create a test

```java
@Testable
class MyTests {

  @Test
  public void myTest() {
    assert true != false;
  }
}
```
