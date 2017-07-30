import java.net.*;

public class InetAddressDemo{
	public static void main(String[] args) throws UnknownHostException {
		InetAddress address = InetAddress.getByName("www.google.com");
		System.out.println(address.toString());
		}
}