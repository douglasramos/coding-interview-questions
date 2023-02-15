Code.require_file("demo.exs", "./elixir")

ExUnit.start()

defmodule DemoTest do
  use ExUnit.Case
  import ExUnit.CaptureIO

  test "hello/1" do
   output = capture_io(fn -> Demo.hello("Jahn") end)
   assert output == "Hello, \e[32m\e[1mJahn\e[0m\n"
  end
end
