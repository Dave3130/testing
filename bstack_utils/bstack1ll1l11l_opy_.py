# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
import os
from uuid import uuid4
from bstack_utils.helper import bstack1l1lll11_opy_, bstack111l11ll111_opy_
from bstack_utils.bstack1l1111ll11_opy_ import bstack11l111l1l11_opy_
class bstack1llll11l_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, started_at=None, framework=None, tags=[], scope=[], bstack111111l11ll_opy_=None, bstack1111111l1l1_opy_=True, bstack1ll1111l1ll_opy_=None, bstack1l11111l1l_opy_=None, result=None, duration=None, bstack1ll1l1l1_opy_=None, meta={}):
        self.bstack1ll1l1l1_opy_ = bstack1ll1l1l1_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack1111111l1l1_opy_:
            self.uuid = uuid4().__str__()
        self.started_at = started_at
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack111111l11ll_opy_ = bstack111111l11ll_opy_
        self.bstack1ll1111l1ll_opy_ = bstack1ll1111l1ll_opy_
        self.bstack1l11111l1l_opy_ = bstack1l11111l1l_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
        self.hooks = []
    def bstack1ll111l1_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack111llll1_opy_(self, meta):
        self.meta = meta
    def bstack11l111l1_opy_(self, hooks):
        self.hooks = hooks
    def bstack1111111ll11_opy_(self):
        bstack111111l1lll_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack11111_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫἻ"): bstack111111l1lll_opy_,
            bstack11111_opy_ (u"ࠩ࡯ࡳࡨࡧࡴࡪࡱࡱࠫἼ"): bstack111111l1lll_opy_,
            bstack11111_opy_ (u"ࠪࡺࡨࡥࡦࡪ࡮ࡨࡴࡦࡺࡨࠨἽ"): bstack111111l1lll_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack11111_opy_ (u"࡚ࠦࡴࡥࡹࡲࡨࡧࡹ࡫ࡤࠡࡣࡵ࡫ࡺࡳࡥ࡯ࡶ࠽ࠤࠧἾ") + key)
            setattr(self, key, val)
    def bstack111111l111l_opy_(self):
        return {
            bstack11111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪἿ"): self.name,
            bstack11111_opy_ (u"࠭ࡢࡰࡦࡼࠫὀ"): {
                bstack11111_opy_ (u"ࠧ࡭ࡣࡱ࡫ࠬὁ"): bstack11111_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨὂ"),
                bstack11111_opy_ (u"ࠩࡦࡳࡩ࡫ࠧὃ"): self.code
            },
            bstack11111_opy_ (u"ࠪࡷࡨࡵࡰࡦࡵࠪὄ"): self.scope,
            bstack11111_opy_ (u"ࠫࡹࡧࡧࡴࠩὅ"): self.tags,
            bstack11111_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨ὆"): self.framework,
            bstack11111_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪ὇"): self.started_at
        }
    def bstack1111111ll1l_opy_(self):
        return {
         bstack11111_opy_ (u"ࠧ࡮ࡧࡷࡥࠬὈ"): self.meta
        }
    def bstack111111l1ll1_opy_(self):
        return {
            bstack11111_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡓࡧࡵࡹࡳࡖࡡࡳࡣࡰࠫὉ"): {
                bstack11111_opy_ (u"ࠩࡵࡩࡷࡻ࡮ࡠࡰࡤࡱࡪ࠭Ὂ"): self.bstack111111l11ll_opy_
            }
        }
    def bstack1111111l111_opy_(self, bstack1111111l1ll_opy_, details):
        step = next(filter(lambda st: st[bstack11111_opy_ (u"ࠪ࡭ࡩ࠭Ὃ")] == bstack1111111l1ll_opy_, self.meta[bstack11111_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪὌ")]), None)
        step.update(details)
    def bstack11l1l11l_opy_(self, bstack1111111l1ll_opy_):
        step = next(filter(lambda st: st[bstack11111_opy_ (u"ࠬ࡯ࡤࠨὍ")] == bstack1111111l1ll_opy_, self.meta[bstack11111_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬ὎")]), None)
        step.update({
            bstack11111_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ὏"): bstack1l1lll11_opy_()
        })
    def bstack1llll1ll_opy_(self, bstack1111111l1ll_opy_, result, duration=None):
        bstack1ll1111l1ll_opy_ = bstack1l1lll11_opy_()
        if bstack1111111l1ll_opy_ is not None and self.meta.get(bstack11111_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧὐ")):
            step = next(filter(lambda st: st[bstack11111_opy_ (u"ࠩ࡬ࡨࠬὑ")] == bstack1111111l1ll_opy_, self.meta[bstack11111_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩὒ")]), None)
            step.update({
                bstack11111_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩὓ"): bstack1ll1111l1ll_opy_,
                bstack11111_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧὔ"): duration if duration else bstack111l11ll111_opy_(step[bstack11111_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪὕ")], bstack1ll1111l1ll_opy_),
                bstack11111_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧὖ"): result.result,
                bstack11111_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩὗ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack1111111lll1_opy_):
        if self.meta.get(bstack11111_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨ὘")):
            self.meta[bstack11111_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩὙ")].append(bstack1111111lll1_opy_)
        else:
            self.meta[bstack11111_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪ὚")] = [ bstack1111111lll1_opy_ ]
    def bstack111111l11l1_opy_(self):
        return {
            bstack11111_opy_ (u"ࠬࡻࡵࡪࡦࠪὛ"): self.bstack1ll111l1_opy_(),
            **self.bstack111111l111l_opy_(),
            **self.bstack1111111ll11_opy_(),
            **self.bstack1111111ll1l_opy_()
        }
    def bstack111111l1l11_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack11111_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ὜"): self.bstack1ll1111l1ll_opy_,
            bstack11111_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡤࡳࡳࠨὝ"): self.duration,
            bstack11111_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨ὞"): self.result.result
        }
        if data[bstack11111_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩὟ")] == bstack11111_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪὠ"):
            data[bstack11111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠪὡ")] = self.result.bstack11111111ll_opy_()
            data[bstack11111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭ὢ")] = [{bstack11111_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩὣ"): self.result.bstack111l1l11l1l_opy_()}]
        return data
    def bstack1111111l11l_opy_(self):
        return {
            bstack11111_opy_ (u"ࠧࡶࡷ࡬ࡨࠬὤ"): self.bstack1ll111l1_opy_(),
            **self.bstack111111l111l_opy_(),
            **self.bstack1111111ll11_opy_(),
            **self.bstack111111l1l11_opy_(),
            **self.bstack1111111ll1l_opy_()
        }
    def bstack1ll1l1ll_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack11111_opy_ (u"ࠨࡕࡷࡥࡷࡺࡥࡥࠩὥ") in event:
            return self.bstack111111l11l1_opy_()
        elif bstack11111_opy_ (u"ࠩࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫὦ") in event:
            return self.bstack1111111l11l_opy_()
    def event_key(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1ll1111l1ll_opy_ = time if time else bstack1l1lll11_opy_()
        self.duration = duration if duration else bstack111l11ll111_opy_(self.started_at, self.bstack1ll1111l1ll_opy_)
        if result:
            self.result = result
class bstack1l1llll1_opy_(bstack1llll11l_opy_):
    def __init__(self, hooks=[], bstack1ll11111_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack1ll11111_opy_ = bstack1ll11111_opy_
        super().__init__(*args, **kwargs, bstack1l11111l1l_opy_=bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࠨὧ"))
    @classmethod
    def bstack111111l1l1l_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack11111_opy_ (u"ࠫ࡮ࡪࠧὨ"): id(step),
                bstack11111_opy_ (u"ࠬࡺࡥࡹࡶࠪὩ"): step.name,
                bstack11111_opy_ (u"࠭࡫ࡦࡻࡺࡳࡷࡪࠧὪ"): step.keyword,
            })
        return bstack1l1llll1_opy_(
            **kwargs,
            meta={
                bstack11111_opy_ (u"ࠧࡧࡧࡤࡸࡺࡸࡥࠨὫ"): {
                    bstack11111_opy_ (u"ࠨࡰࡤࡱࡪ࠭Ὤ"): feature.name,
                    bstack11111_opy_ (u"ࠩࡳࡥࡹ࡮ࠧὭ"): feature.filename,
                    bstack11111_opy_ (u"ࠪࡨࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠨὮ"): feature.description
                },
                bstack11111_opy_ (u"ࠫࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭Ὧ"): {
                    bstack11111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪὰ"): scenario.name
                },
                bstack11111_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬά"): steps,
                bstack11111_opy_ (u"ࠧࡦࡺࡤࡱࡵࡲࡥࡴࠩὲ"): bstack11l111l1l11_opy_(test)
            }
        )
    def bstack111111l1111_opy_(self):
        return {
            bstack11111_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧέ"): self.hooks
        }
    def bstack1111111llll_opy_(self):
        if self.bstack1ll11111_opy_:
            return {
                bstack11111_opy_ (u"ࠩ࡬ࡲࡹ࡫ࡧࡳࡣࡷ࡭ࡴࡴࡳࠨὴ"): self.bstack1ll11111_opy_
            }
        return {}
    def bstack1111111l11l_opy_(self):
        return {
            **super().bstack1111111l11l_opy_(),
            **self.bstack111111l1111_opy_()
        }
    def bstack111111l11l1_opy_(self):
        return {
            **super().bstack111111l11l1_opy_(),
            **self.bstack1111111llll_opy_()
        }
    def event_key(self):
        return bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࠬή")
class bstack1ll11lll_opy_(bstack1llll11l_opy_):
    def __init__(self, hook_type, *args,bstack1ll11111_opy_={}, **kwargs):
        self.hook_type = hook_type
        self.bstack1l1111l111l_opy_ = None
        self.bstack1ll11111_opy_ = bstack1ll11111_opy_
        super().__init__(*args, **kwargs, bstack1l11111l1l_opy_=bstack11111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩὶ"))
    def bstack1l1111ll_opy_(self):
        return self.hook_type
    def bstack11111111lll_opy_(self):
        return {
            bstack11111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨί"): self.hook_type
        }
    def bstack1111111l11l_opy_(self):
        return {
            **super().bstack1111111l11l_opy_(),
            **self.bstack11111111lll_opy_()
        }
    def bstack111111l11l1_opy_(self):
        return {
            **super().bstack111111l11l1_opy_(),
            bstack11111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠ࡫ࡧࠫὸ"): self.bstack1l1111l111l_opy_,
            **self.bstack11111111lll_opy_()
        }
    def event_key(self):
        return bstack11111_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࠩό")
    def bstack11l1l111_opy_(self, bstack1l1111l111l_opy_):
        self.bstack1l1111l111l_opy_ = bstack1l1111l111l_opy_