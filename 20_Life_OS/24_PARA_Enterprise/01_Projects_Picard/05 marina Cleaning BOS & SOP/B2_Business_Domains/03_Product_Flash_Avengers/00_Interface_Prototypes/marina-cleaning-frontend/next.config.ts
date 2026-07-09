/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'standalone', // Requis pour une image Docker optimisée
  eslint: {
    ignoreDuringBuilds: true,
  },
  typescript: {
    ignoreBuildErrors: true,
  }
};

export default nextConfig;
