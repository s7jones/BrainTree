#pragma once

#include "../Composite.h"
#include <cassert>

namespace BrainTree
{

// The Selector composite ticks each child node in order.
// If a child succeeds or runs, the selector returns the same status.
// In the next tick, it will try to run each child in order again.
// If all children fails, only then does the selector fail.
class Selector : public Composite
{
public:
    void initialize() override
    {
        it = children.begin();
    }

    Status update() override
    {
        assert(hasChildren() && "Composite has no children");

        while (it != children.end()) {
            auto status = (*it)->tick();

            if (status != Status::Failure) {
                return status;
            }

            it++;
        }

        return Status::Failure;
    }
};

}