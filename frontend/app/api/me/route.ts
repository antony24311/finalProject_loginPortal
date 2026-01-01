import { NextResponse } from "next/server";

export async function GET(req: Request) {
  const auth = req.headers.get("authorization");

  if (!auth) {
    return NextResponse.json(
      { error: "Not authenticated" },
      { status: 401 }
    );
  }

  const backendUrl = process.env.BACKEND_URL;
  if (!backendUrl) {
    return NextResponse.json(
      { error: "BACKEND_URL not set" },
      { status: 500 }
    );
  }

  const res = await fetch(`${backendUrl}/api/me`, {
    headers: {
      Authorization: auth, // ⭐ 原封不動轉送
    },
  });

  const data = await res.json();
  return NextResponse.json(data, { status: res.status });
}
