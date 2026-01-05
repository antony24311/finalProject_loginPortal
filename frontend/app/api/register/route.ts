import { NextResponse } from "next/server";

export async function POST(req: Request) {
  const body = await req.json();

  const backendUrl = process.env.BACKEND_URL;
  if (!backendUrl) {
    return NextResponse.json(
      { error: "BACKEND_URL not set" },
      { status: 500 }
    );
  }

  console.log("REGISTER payload =", body);
  console.log("Proxy register to:", `${backendUrl}/api/register`);

  const res = await fetch(`${backendUrl}/api/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });

  const text = await res.text();
  console.log("REGISTER backend response =", text);

  return NextResponse.json(JSON.parse(text), { status: res.status });
}
