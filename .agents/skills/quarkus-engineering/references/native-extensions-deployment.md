# Quarkus Native, Extensions & Deployment

Native-image compatibility can require reflection/resource/proxy registration or replacement of unsupported dynamic behavior. Verify libraries under native build early when production requires native output.

Prefer versions managed by the Quarkus platform/BOM. A library or extension version that compiles independently may still be incompatible with build-time augmentation.
