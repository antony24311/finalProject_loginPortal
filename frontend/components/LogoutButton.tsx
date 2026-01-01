"use client";

export default function LogoutButton() {
  const logout = () => {
    localStorage.removeItem("access_token");
    window.location.href = "/";
  };

  return <button onClick={logout}>Logout</button>;
}
