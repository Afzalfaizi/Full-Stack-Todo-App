import { Button } from "@/components/ui/button"
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import AddTask from "./AddTask"
import { Children } from "react"
import EditTask from "./EditTask"

export function Modal({children, title, Adding, Editing}:{children:React.ReactNode, title:string,
   Adding?:boolean, Editing?:boolean}) {
  return (
    <Dialog>
      <DialogTrigger asChild>
        {children}
      </DialogTrigger>
      <DialogContent className="sm:max-w-[425px]">
        <DialogHeader>
          <DialogTitle>{title}</DialogTitle>
        </DialogHeader>
        {Adding && <AddTask/>}
        {Editing && <EditTask/>}
      </DialogContent>
    </Dialog>
  )
}
