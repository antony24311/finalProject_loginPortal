"use client";

import { useEffect, useState } from "react";
import LogoutButton from "@/components/LogoutButton";

type User = {
  id: number;
  username: string;
};

export default function DashboardPage() {
  const [user, setUser] = useState<User | null>(null);

  useEffect(() => {
    const token = localStorage.getItem("access_token");

    if (!token) {
      window.location.href = "/";
      return;
    }

    fetch("/api/me", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
      .then(async (res) => {
        if (!res.ok) throw new Error("unauthorized");
        return res.json();
      })
      .then((data) => setUser(data))
      .catch(() => {
        alert("尚未登入");
        localStorage.removeItem("access_token");
        window.location.href = "/";
      });
  }, []);

  if (!user) return <p>Loading...</p>;

  return (
    <main style={{ padding: 40 }}>
      <h1>Dashboard</h1>
      <p>Welcome, {user.username}</p>
      <LogoutButton />
    </main>
  );
}
