# fn

```
curl -LSs https://raw.githubusercontent.com/fnproject/cli/master/install | sh

fn start

fn list contexts

fn use context default

// To use Fn for local development, set the registry to an arbitrary value
fn update context registry fndemouser

//To use Fn for normal development, set the registry to your Docker Hub user name
fn update context registry your-docker-hub-user-name

```


# fn - Python

```
//The --runtime option is used to indicate that the function we’re going to develop will be written in Python

fn init --runtime python pythonfn

//it will create a pythonfn directory

func.py
- contains your actual Python function is generated along with several supporting files



func.yml

-  schema_version–identifies the version of the schema for  this function file. Essentially, it determines which fields are present in func.yaml.
-  name–the name of the function. Matches the directory name.
-  version–automatically starting at 0.0.1.
-  runtime–the name of the runtime/language which was set based on the value set in --runtime.
-  memory–The max memory size for a function in megabytes.
-  entrypoint–the name of the executable to invoke when your function is called


requirements.txt
– specifies all the dependencies for your Python function

```

```
fn create app pythonapp

fn --verbose deploy --app pythonapp --local

fn list apps

fn list functions pythonapp

```

```
// Invoke your Deployed Function
fn invoke pythonapp pythonfn

// Getting a Function’s Invoke Endpoint

fn inspect function pythonapp pythonfn
curl -X "POST" -H "Content-Type: application/json" http://localhost:8080/invoke/01H6F3G6SPNG8G00GZJ0000001

```







