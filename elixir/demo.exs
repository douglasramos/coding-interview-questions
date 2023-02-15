# demo.exs
Mix.install([
  {:bunt, "~> 0.2.0"}
])

defmodule Demo do
  def hello(name \\ "John") do
    ["Hello, ", :green, :bright, name]
    |> Bunt.ANSI.format
    |> IO.puts
  end
end

Demo.hello("Smahi")
