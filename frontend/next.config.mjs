/** @type {import('next').NextConfig} */
// Control whether to allow inline scripts via an environment variable.
// - To allow inline scripts (dev): set ALLOW_INLINE_SCRIPTS=true
// - In production omit the env var or set it to false.
const allowInline = process.env.ALLOW_INLINE_SCRIPTS === 'true' || process.env.NODE_ENV !== 'production'

const scriptSrc = allowInline
  ? "script-src 'self' 'unsafe-eval' 'unsafe-inline' https://va.vercel-scripts.com;"
  : "script-src 'self' 'unsafe-eval' https://va.vercel-scripts.com;"

const securityHeaders = [
  {
    key: "Content-Security-Policy",
    value: `
      default-src 'self';
      ${scriptSrc}
      style-src 'self' 'unsafe-inline';
      img-src 'self' data:;
      connect-src 'self' http://127.0.0.1:8000 http://localhost:4000 ws:;
      frame-ancestors 'none';
      base-uri 'self';
      form-action 'self';
    `.replace(/\s{2,}/g, " ").trim(),
  },
  { key: "X-Frame-Options", value: "DENY" },
  { key: "X-Content-Type-Options", value: "nosniff" },
  { key: "X-XSS-Protection", value: "1; mode=block" },
  { key: "Referrer-Policy", value: "no-referrer" },
  { key: "Permissions-Policy", value: "geolocation=(), microphone=(), camera=()" },
  { key: "Strict-Transport-Security", value: "max-age=31536000; includeSubDomains" },
  { key: "X-Powered-By", value: "" },
];

const nextConfig = {
  typescript: {
    ignoreBuildErrors: true,
  },
  images: {
    unoptimized: true,
  },

  async rewrites() {
    return [
      {
        source: "/api/:path*",
        destination: "http://127.0.0.1:8000/api/:path*",
      },
    ];
  },

  async headers() {
    return [
      {
        source: "/(.*)",
        headers: securityHeaders,
      },
    ];
  },
};

export default nextConfig;
