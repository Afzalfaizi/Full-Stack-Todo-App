import { Modal } from "@/components/Modal";
import TodoTable from "@/components/TodoTable";

export default function Home() {
  return (
    <main className=" max-w-5xl mx-auto mt-8">
      {/* Add Task Section */}
      <section>
        <Modal/>
      </section>
      {/* Todo Table */}
      <section className=" mt-4">
        <TodoTable/>

      </section>
      
    </main>
  );
}
