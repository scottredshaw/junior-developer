import Image from "next/image";
import { Suspense } from "react";


import Content from "@/components/Content";

async function ContentList() {
  try {
      const response = await fetch("http://localhost:8000/data");
      if (!response.ok) {
        throw new Error(`HTTP error: ${response.status}`);
      }
      const data = await response.json();

      return (
        <>
          {data.map((item, index) => (
            <Content
              key={index}
              category={item.category}
              question={item.question}
              sources={item.sources}
              content={item.content}
            />
          ))}
        </>
      );
    }
    catch (error) {
      console.error("Error fetching JSON:", error);
    }
}

export default function Home() {
  return (
    <main className="mx-auto flex max-w-3xl flex-col items-center gap-8 p-8">
      <div className="flex flex-col items-center text-center">
        <Image
          src="/logo.png"
          alt="Citizens Advice SORT"
          width={150}
          height={150}
          priority
        />
        <h1 className="mt-4 text-2xl font-bold">Citizens Advice SORT</h1>
        <h2 className="text-lg font-medium">Junior Developer Practical</h2>
      </div>
      {/* Anything that fetches data goes inside Suspense, which shows the fallback until it's ready */}
      <Suspense fallback={<p>Loading...</p>}>
        <ContentList />
      </Suspense>
    </main>
  );
}
