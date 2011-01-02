namespace nixon
{
	using System;
	using Magnum;
	
	public class Bob
	{
		public Bob()
		{
		    int i = 0;
			G = CombGuid.Generate();
		}
		public Guid G;
		public string Name = "nixon";
	}
}