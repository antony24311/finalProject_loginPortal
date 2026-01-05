import { NextResponse } from "next/server";

export async function POST(req: Request) {
  const isDev = process.env.NODE_ENV !== "production";

  try {
    const body = await req.json();

    if (isDev) {
      console.log("=== /api/login called ===");
      console.log("Request body:", body);
    }

    const backendUrl = process.env.BACKEND_URL;
    if (!backendUrl) {
      // 系統設定錯誤，不應洩漏細節
      return NextResponse.json(
        { error: "Service configuration error" },
        { status: 500 }
      );
    }

    const target = `${backendUrl}/api/login`;
    if (isDev) {
      console.log("Proxy to:", target);
    }

    const res = await fetch(target, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });

    const text = await res.text();

    if (isDev) {
      console.log("Backend response status:", res.status);
      console.log("Backend raw response:", text);
    }

    // 防止後端回傳非 JSON 造成系統崩潰
    let data: unknown;
    try {
      data = JSON.parse(text);
    } catch {
      return NextResponse.json(
        { error: "Invalid response from authentication service" },
        { status: 502 }
      );
    }

    return NextResponse.json(data, { status: res.status });

  } catch (err) {
    if (isDev) {
      console.error("LOGIN PROXY ERROR:", err);
    }

    return NextResponse.json(
      { error: "Authentication service unavailable" },
      { status: 502 }
    );
  }
}
