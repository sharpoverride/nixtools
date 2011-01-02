namespace tests
{
	using Xunit;
	using nixon;
	
	public class Sample
	{
		[Fact]
		public void Bill()
		{
			var b = new Bob();
			Assert.Equal("nixon",b.Name);
		}
	}
}