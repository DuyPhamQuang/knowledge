resource "aws_instance" "web" {
  # ...

  # Establishes connection to be used by all
  # generic remote provisioners (i.e. file/remote-exec)
  connection {
    type     = "ssh"
    user     = "root"
    password = 123
    host     = "192.168.56.3"
  }

  provisioner "remote-exec" {
    inline = [
      "ls -l",
      "echo \"Ok\""
    ]
  }
}
