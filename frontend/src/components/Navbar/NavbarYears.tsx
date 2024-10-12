import { Label } from "@/components/ui/label"
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"

export default function Years() {
  return (
    <RadioGroup defaultValue="comfortable">
      <div className="flex items-center mx-3 space-x-2">
        <RadioGroupItem value="default" id="r1" />
        <Label htmlFor="r1">2025</Label>
      </div>
      <div className="flex items-center mx-3 space-x-2">
        <RadioGroupItem value="comfortable" id="r2" />
        <Label htmlFor="r2">2026</Label>
      </div>
      <div className="flex items-center mx-3 space-x-2">
        <RadioGroupItem value="compact" id="r3" />
        <Label htmlFor="r3">2027</Label>
      </div>
    </RadioGroup>
  )
}
