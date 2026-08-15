# Rails Hotwire, Auth & Rollouts

Hotwire can preserve server-side ownership for many interactive flows; use a heavier client state/API boundary only when product behavior requires it.

Authorization is action/resource specific. Strong Parameters constrain writes but do not authorize records; serializers/views constrain output but do not authorize the action.

For rolling deploys, make schema changes compatible with both old and new app processes before destructive cleanup.
