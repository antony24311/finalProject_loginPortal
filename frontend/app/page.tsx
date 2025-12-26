"use client"

import type React from "react"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"

export default function AuthPage() {
  const [mode, setMode] = useState<"login" | "register">("login")
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")


  // 在 handleSubmit 內修改
const handleSubmit = async (e: React.FormEvent) => {
  e.preventDefault();
  
  // 1. 決定要呼叫登入還是註冊 API
  const apiEndpoint = mode === "login" ? "/api/login" : "/api/register";

  try {
    const response = await fetch(apiEndpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ username, password }), // 對應你 FastAPI 的 Schema
    });

    const data = await response.json();

    if (response.ok) {
      if (mode === "login") {
        alert("登入成功！正在跳轉...");
        window.location.href = "/dashboard"; // 登入成功後去儀表板
      } else {
        alert("註冊成功！請登入");
        setMode("login"); // 註冊完切換回登入模式
      }
    } else {
      alert(`失敗：${data.detail || "伺服器錯誤"}`);
    }
  } catch (error) {
    alert("連線失敗，請檢查 API 是否啟動");
  }
};

  // const handleSubmit = (e: React.FormEvent) => {
  //   e.preventDefault()
  //   console.log("[v0] Form submitted:", { mode, username, password })
  //   // Handle form submission logic here
  //   alert(`${mode === "login" ? "Login" : "Register"} submitted with username: ${username}`)
  // }

  return (
    <div
      className={`min-h-screen flex items-center justify-center p-4 relative overflow-hidden transition-all duration-700 ${
        mode === "login"
          ? "bg-gradient-to-br from-slate-900 via-blue-950 to-indigo-900"
          : "bg-gradient-to-br from-purple-950 via-pink-950 to-rose-950"
      }`}
    >
      <div className="absolute inset-0 overflow-hidden">
        {mode === "login" ? (
          <>
            <div className="absolute -top-40 -left-40 w-[600px] h-[600px] bg-gradient-to-br from-cyan-500/40 to-blue-600/30 rotate-45 blur-3xl transition-all duration-700" />
            <div className="absolute top-20 right-20 w-[500px] h-[500px] bg-gradient-to-br from-blue-500/35 to-indigo-600/25 -rotate-45 blur-2xl transition-all duration-700" />
            <div className="absolute bottom-0 left-1/4 w-[600px] h-[400px] bg-gradient-to-tr from-cyan-400/30 to-blue-500/20 rotate-12 blur-3xl transition-all duration-700" />
            <div className="absolute -bottom-40 -right-40 w-[500px] h-[500px] bg-gradient-to-tl from-indigo-500/35 to-blue-600/25 -rotate-12 blur-2xl transition-all duration-700" />

            <div
              className="absolute top-1/4 left-1/3 w-80 h-80 bg-gradient-to-br from-cyan-400/20 to-transparent rotate-45 transition-all duration-700"
              style={{ clipPath: "polygon(0 0, 100% 0, 100% 100%, 0 100%)" }}
            />
            <div
              className="absolute bottom-1/3 right-1/4 w-96 h-96 bg-gradient-to-tl from-blue-400/20 to-transparent -rotate-45 transition-all duration-700"
              style={{ clipPath: "polygon(0 0, 100% 0, 50% 100%)" }}
            />
            <div
              className="absolute top-1/2 right-1/3 w-64 h-64 bg-gradient-to-br from-indigo-400/15 to-transparent -rotate-12 transition-all duration-700"
              style={{ clipPath: "polygon(50% 0, 100% 50%, 50% 100%, 0 50%)" }}
            />
          </>
        ) : (
          <>
            <div className="absolute -top-40 -left-40 w-[600px] h-[600px] bg-gradient-to-br from-fuchsia-500/40 to-purple-600/30 -rotate-12 blur-3xl transition-all duration-700" />
            <div className="absolute top-20 right-20 w-[500px] h-[500px] bg-gradient-to-br from-pink-500/35 to-rose-600/25 rotate-45 blur-2xl transition-all duration-700" />
            <div className="absolute bottom-0 left-1/4 w-[600px] h-[400px] bg-gradient-to-tr from-purple-400/30 to-fuchsia-500/20 -rotate-45 blur-3xl transition-all duration-700" />
            <div className="absolute -bottom-40 -right-40 w-[500px] h-[500px] bg-gradient-to-tl from-rose-500/35 to-pink-600/25 rotate-12 blur-2xl transition-all duration-700" />

            <div
              className="absolute top-1/4 left-1/3 w-80 h-80 bg-gradient-to-br from-fuchsia-400/20 to-transparent -rotate-45 transition-all duration-700"
              style={{ clipPath: "polygon(50% 0, 100% 100%, 0 100%)" }}
            />
            <div
              className="absolute bottom-1/3 right-1/4 w-96 h-96 bg-gradient-to-tl from-pink-400/20 to-transparent rotate-45 transition-all duration-700"
              style={{ clipPath: "polygon(0 0, 100% 0, 100% 100%)" }}
            />
            <div
              className="absolute top-1/2 right-1/3 w-64 h-64 bg-gradient-to-br from-rose-400/15 to-transparent -rotate-12 transition-all duration-700"
              style={{ clipPath: "polygon(25% 0, 100% 0, 75% 100%, 0 100%)" }}
            />
          </>
        )}

        <div className="absolute inset-0 bg-[linear-gradient(45deg,transparent_48%,#ffffff03_49%,#ffffff03_51%,transparent_52%)] bg-[size:40px_40px]" />
        <div className="absolute inset-0 bg-[linear-gradient(-45deg,transparent_48%,#ffffff02_49%,#ffffff02_51%,transparent_52%)] bg-[size:40px_40px]" />
      </div>

      <Card className="w-full max-w-md relative z-10 backdrop-blur-xl bg-background/80 border-white/20 shadow-2xl">
        <CardHeader className="space-y-1">
          <CardTitle className="text-2xl font-bold text-center">
            {mode === "login" ? "Welcome Back" : "Create Account"}
          </CardTitle>
          <CardDescription className="text-center">
            {mode === "login"
              ? "Enter your credentials to access your account"
              : "Fill in your details to create a new account"}
          </CardDescription>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleSubmit} className="space-y-4">
            <div className="space-y-2">
              <Label htmlFor="username">Username</Label>
              <Input
                id="username"
                type="text"
                placeholder="Enter your username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
              />
            </div>

            <div className="space-y-2">
              <Label htmlFor="password">Password</Label>
              <Input
                id="password"
                type="password"
                placeholder="Enter your password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>

            <Button
              type="submit"
              className={`w-full transition-all ${
                mode === "login"
                  ? "bg-blue-600 hover:bg-blue-700 shadow-lg shadow-blue-500/30"
                  : "bg-purple-600 hover:bg-purple-700 shadow-lg shadow-purple-500/30"
              }`}
              size="lg"
            >
              {mode === "login" ? "Login" : "Register"}
            </Button>

            <div className="text-center text-sm">
              {mode === "login" ? (
                <p className="text-muted-foreground">
                  Don't have an account?{" "}
                  <button
                    type="button"
                    onClick={() => setMode("register")}
                    className="text-purple-400 hover:text-purple-300 underline underline-offset-4 font-medium transition-colors"
                  >
                    Register here
                  </button>
                </p>
              ) : (
                <p className="text-muted-foreground">
                  Already have an account?{" "}
                  <button
                    type="button"
                    onClick={() => setMode("login")}
                    className="text-blue-400 hover:text-blue-300 underline underline-offset-4 font-medium transition-colors"
                  >
                    Login here
                  </button>
                </p>
              )}
            </div>
          </form>
        </CardContent>
      </Card>
    </div>
  )
}
