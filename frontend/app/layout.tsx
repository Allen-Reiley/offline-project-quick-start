import type { Metadata } from "next";
import "./globals.css";
import Providers from "./providers"; // Import our new provider

export const metadata: Metadata = {
  title: "AuraWorks Master Seed",
  description: "Industrial Intelligence Engine",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}