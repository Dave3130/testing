# coding: UTF-8
import sys
bstack11l111_opy_ = sys.version_info [0] == 2
bstack1l11ll_opy_ = 2048
bstack1l1l11_opy_ = 7
def bstack11l1111_opy_ (bstack111l11l_opy_):
    global bstack1ll1l1l_opy_
    bstack1ll1ll_opy_ = ord (bstack111l11l_opy_ [-1])
    bstack1lll11_opy_ = bstack111l11l_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1ll_opy_ % len (bstack1lll11_opy_)
    bstack1l1l1ll_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l111_opy_:
        bstack1l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack1l11_opy_ = str () .join ([chr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack1l11_opy_)
import os
from uuid import uuid4
from bstack_utils.helper import bstack1ll11lll_opy_, bstack1111l1111l1_opy_
from bstack_utils.bstack1l1ll1111_opy_ import bstack11l111l11l1_opy_
class bstack1l1ll11l_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, started_at=None, framework=None, tags=[], scope=[], bstack1111111l1ll_opy_=None, bstack11111111lll_opy_=True, bstack1l1lll1l1l1_opy_=None, bstack111ll11l1l_opy_=None, result=None, duration=None, bstack1lll1l11_opy_=None, meta={}):
        self.bstack1lll1l11_opy_ = bstack1lll1l11_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack11111111lll_opy_:
            self.uuid = uuid4().__str__()
        self.started_at = started_at
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack1111111l1ll_opy_ = bstack1111111l1ll_opy_
        self.bstack1l1lll1l1l1_opy_ = bstack1l1lll1l1l1_opy_
        self.bstack111ll11l1l_opy_ = bstack111ll11l1l_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
        self.hooks = []
    def bstack1llll1l1_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack11l1l111_opy_(self, meta):
        self.meta = meta
    def bstack11l11l11_opy_(self, hooks):
        self.hooks = hooks
    def bstack111111l11ll_opy_(self):
        bstack111111l1111_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack11l1111_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪἺ"): bstack111111l1111_opy_,
            bstack11l1111_opy_ (u"ࠨ࡮ࡲࡧࡦࡺࡩࡰࡰࠪἻ"): bstack111111l1111_opy_,
            bstack11l1111_opy_ (u"ࠩࡹࡧࡤ࡬ࡩ࡭ࡧࡳࡥࡹ࡮ࠧἼ"): bstack111111l1111_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack11l1111_opy_ (u"࡙ࠥࡳ࡫ࡸࡱࡧࡦࡸࡪࡪࠠࡢࡴࡪࡹࡲ࡫࡮ࡵ࠼ࠣࠦἽ") + key)
            setattr(self, key, val)
    def bstack1111111ll11_opy_(self):
        return {
            bstack11l1111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩἾ"): self.name,
            bstack11l1111_opy_ (u"ࠬࡨ࡯ࡥࡻࠪἿ"): {
                bstack11l1111_opy_ (u"࠭࡬ࡢࡰࡪࠫὀ"): bstack11l1111_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧὁ"),
                bstack11l1111_opy_ (u"ࠨࡥࡲࡨࡪ࠭ὂ"): self.code
            },
            bstack11l1111_opy_ (u"ࠩࡶࡧࡴࡶࡥࡴࠩὃ"): self.scope,
            bstack11l1111_opy_ (u"ࠪࡸࡦ࡭ࡳࠨὄ"): self.tags,
            bstack11l1111_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧὅ"): self.framework,
            bstack11l1111_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩ὆"): self.started_at
        }
    def bstack1111111llll_opy_(self):
        return {
         bstack11l1111_opy_ (u"࠭࡭ࡦࡶࡤࠫ὇"): self.meta
        }
    def bstack111111l111l_opy_(self):
        return {
            bstack11l1111_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡒࡦࡴࡸࡲࡕࡧࡲࡢ࡯ࠪὈ"): {
                bstack11l1111_opy_ (u"ࠨࡴࡨࡶࡺࡴ࡟࡯ࡣࡰࡩࠬὉ"): self.bstack1111111l1ll_opy_
            }
        }
    def bstack111111l1l11_opy_(self, bstack111111l11l1_opy_, details):
        step = next(filter(lambda st: st[bstack11l1111_opy_ (u"ࠩ࡬ࡨࠬὊ")] == bstack111111l11l1_opy_, self.meta[bstack11l1111_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩὋ")]), None)
        step.update(details)
    def bstack11l11ll1_opy_(self, bstack111111l11l1_opy_):
        step = next(filter(lambda st: st[bstack11l1111_opy_ (u"ࠫ࡮ࡪࠧὌ")] == bstack111111l11l1_opy_, self.meta[bstack11l1111_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫὍ")]), None)
        step.update({
            bstack11l1111_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪ὎"): bstack1ll11lll_opy_()
        })
    def bstack1ll1llll_opy_(self, bstack111111l11l1_opy_, result, duration=None):
        bstack1l1lll1l1l1_opy_ = bstack1ll11lll_opy_()
        if bstack111111l11l1_opy_ is not None and self.meta.get(bstack11l1111_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭὏")):
            step = next(filter(lambda st: st[bstack11l1111_opy_ (u"ࠨ࡫ࡧࠫὐ")] == bstack111111l11l1_opy_, self.meta[bstack11l1111_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨὑ")]), None)
            step.update({
                bstack11l1111_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨὒ"): bstack1l1lll1l1l1_opy_,
                bstack11l1111_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭ὓ"): duration if duration else bstack1111l1111l1_opy_(step[bstack11l1111_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩὔ")], bstack1l1lll1l1l1_opy_),
                bstack11l1111_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ὕ"): result.result,
                bstack11l1111_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨὖ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack1111111l111_opy_):
        if self.meta.get(bstack11l1111_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧὗ")):
            self.meta[bstack11l1111_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨ὘")].append(bstack1111111l111_opy_)
        else:
            self.meta[bstack11l1111_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩὙ")] = [ bstack1111111l111_opy_ ]
    def bstack1111111lll1_opy_(self):
        return {
            bstack11l1111_opy_ (u"ࠫࡺࡻࡩࡥࠩ὚"): self.bstack1llll1l1_opy_(),
            **self.bstack1111111ll11_opy_(),
            **self.bstack111111l11ll_opy_(),
            **self.bstack1111111llll_opy_()
        }
    def bstack1111111ll1l_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack11l1111_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪὛ"): self.bstack1l1lll1l1l1_opy_,
            bstack11l1111_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡣࡲࡹࠧ὜"): self.duration,
            bstack11l1111_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧὝ"): self.result.result
        }
        if data[bstack11l1111_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨ὞")] == bstack11l1111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩὟ"):
            data[bstack11l1111_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠩὠ")] = self.result.bstack11111111ll_opy_()
            data[bstack11l1111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬὡ")] = [{bstack11l1111_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨὢ"): self.result.bstack111l1111ll1_opy_()}]
        return data
    def bstack111111l1ll1_opy_(self):
        return {
            bstack11l1111_opy_ (u"࠭ࡵࡶ࡫ࡧࠫὣ"): self.bstack1llll1l1_opy_(),
            **self.bstack1111111ll11_opy_(),
            **self.bstack111111l11ll_opy_(),
            **self.bstack1111111ll1l_opy_(),
            **self.bstack1111111llll_opy_()
        }
    def bstack1l11lll1_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack11l1111_opy_ (u"ࠧࡔࡶࡤࡶࡹ࡫ࡤࠨὤ") in event:
            return self.bstack1111111lll1_opy_()
        elif bstack11l1111_opy_ (u"ࠨࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪὥ") in event:
            return self.bstack111111l1ll1_opy_()
    def event_key(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1l1lll1l1l1_opy_ = time if time else bstack1ll11lll_opy_()
        self.duration = duration if duration else bstack1111l1111l1_opy_(self.started_at, self.bstack1l1lll1l1l1_opy_)
        if result:
            self.result = result
class bstack11llllll_opy_(bstack1l1ll11l_opy_):
    def __init__(self, hooks=[], bstack1l1l1lll_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack1l1l1lll_opy_ = bstack1l1l1lll_opy_
        super().__init__(*args, **kwargs, bstack111ll11l1l_opy_=bstack11l1111_opy_ (u"ࠩࡷࡩࡸࡺࠧὦ"))
    @classmethod
    def bstack111111l1l1l_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack11l1111_opy_ (u"ࠪ࡭ࡩ࠭ὧ"): id(step),
                bstack11l1111_opy_ (u"ࠫࡹ࡫ࡸࡵࠩὨ"): step.name,
                bstack11l1111_opy_ (u"ࠬࡱࡥࡺࡹࡲࡶࡩ࠭Ὡ"): step.keyword,
            })
        return bstack11llllll_opy_(
            **kwargs,
            meta={
                bstack11l1111_opy_ (u"࠭ࡦࡦࡣࡷࡹࡷ࡫ࠧὪ"): {
                    bstack11l1111_opy_ (u"ࠧ࡯ࡣࡰࡩࠬὫ"): feature.name,
                    bstack11l1111_opy_ (u"ࠨࡲࡤࡸ࡭࠭Ὤ"): feature.filename,
                    bstack11l1111_opy_ (u"ࠩࡧࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧὭ"): feature.description
                },
                bstack11l1111_opy_ (u"ࠪࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬὮ"): {
                    bstack11l1111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩὯ"): scenario.name
                },
                bstack11l1111_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫὰ"): steps,
                bstack11l1111_opy_ (u"࠭ࡥࡹࡣࡰࡴࡱ࡫ࡳࠨά"): bstack11l111l11l1_opy_(test)
            }
        )
    def bstack1111111l1l1_opy_(self):
        return {
            bstack11l1111_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭ὲ"): self.hooks
        }
    def bstack1111111l11l_opy_(self):
        if self.bstack1l1l1lll_opy_:
            return {
                bstack11l1111_opy_ (u"ࠨ࡫ࡱࡸࡪ࡭ࡲࡢࡶ࡬ࡳࡳࡹࠧέ"): self.bstack1l1l1lll_opy_
            }
        return {}
    def bstack111111l1ll1_opy_(self):
        return {
            **super().bstack111111l1ll1_opy_(),
            **self.bstack1111111l1l1_opy_()
        }
    def bstack1111111lll1_opy_(self):
        return {
            **super().bstack1111111lll1_opy_(),
            **self.bstack1111111l11l_opy_()
        }
    def event_key(self):
        return bstack11l1111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫὴ")
class bstack1ll11ll1_opy_(bstack1l1ll11l_opy_):
    def __init__(self, hook_type, *args,bstack1l1l1lll_opy_={}, **kwargs):
        self.hook_type = hook_type
        self.bstack1l111l1lll1_opy_ = None
        self.bstack1l1l1lll_opy_ = bstack1l1l1lll_opy_
        super().__init__(*args, **kwargs, bstack111ll11l1l_opy_=bstack11l1111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨή"))
    def bstack1l11l11l_opy_(self):
        return self.hook_type
    def bstack11111111ll1_opy_(self):
        return {
            bstack11l1111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧὶ"): self.hook_type
        }
    def bstack111111l1ll1_opy_(self):
        return {
            **super().bstack111111l1ll1_opy_(),
            **self.bstack11111111ll1_opy_()
        }
    def bstack1111111lll1_opy_(self):
        return {
            **super().bstack1111111lll1_opy_(),
            bstack11l1111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡪࡦࠪί"): self.bstack1l111l1lll1_opy_,
            **self.bstack11111111ll1_opy_()
        }
    def event_key(self):
        return bstack11l1111_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࠨὸ")
    def bstack11l1l1ll_opy_(self, bstack1l111l1lll1_opy_):
        self.bstack1l111l1lll1_opy_ = bstack1l111l1lll1_opy_