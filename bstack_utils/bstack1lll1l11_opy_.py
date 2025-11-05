# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
import os
from uuid import uuid4
from bstack_utils.helper import bstack1ll111ll_opy_, bstack111l1l11ll1_opy_
from bstack_utils.bstack11111ll1l1_opy_ import bstack11l111l1111_opy_
class bstack1ll11l1l_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, started_at=None, framework=None, tags=[], scope=[], bstack111111l1l11_opy_=None, bstack111111l1lll_opy_=True, bstack1ll11ll1lll_opy_=None, bstack11l1l1ll11_opy_=None, result=None, duration=None, bstack1l1l1111_opy_=None, meta={}):
        self.bstack1l1l1111_opy_ = bstack1l1l1111_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack111111l1lll_opy_:
            self.uuid = uuid4().__str__()
        self.started_at = started_at
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack111111l1l11_opy_ = bstack111111l1l11_opy_
        self.bstack1ll11ll1lll_opy_ = bstack1ll11ll1lll_opy_
        self.bstack11l1l1ll11_opy_ = bstack11l1l1ll11_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
        self.hooks = []
    def bstack1ll11111_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack111lllll_opy_(self, meta):
        self.meta = meta
    def bstack11l111ll_opy_(self, hooks):
        self.hooks = hooks
    def bstack1111111l111_opy_(self):
        bstack1111111lll1_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack11ll1ll_opy_ (u"ࠩࡩ࡭ࡱ࡫࡟࡯ࡣࡰࡩࠬἼ"): bstack1111111lll1_opy_,
            bstack11ll1ll_opy_ (u"ࠪࡰࡴࡩࡡࡵ࡫ࡲࡲࠬἽ"): bstack1111111lll1_opy_,
            bstack11ll1ll_opy_ (u"ࠫࡻࡩ࡟ࡧ࡫࡯ࡩࡵࡧࡴࡩࠩἾ"): bstack1111111lll1_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack11ll1ll_opy_ (u"࡛ࠧ࡮ࡦࡺࡳࡩࡨࡺࡥࡥࠢࡤࡶ࡬ࡻ࡭ࡦࡰࡷ࠾ࠥࠨἿ") + key)
            setattr(self, key, val)
    def bstack1111111l1l1_opy_(self):
        return {
            bstack11ll1ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫὀ"): self.name,
            bstack11ll1ll_opy_ (u"ࠧࡣࡱࡧࡽࠬὁ"): {
                bstack11ll1ll_opy_ (u"ࠨ࡮ࡤࡲ࡬࠭ὂ"): bstack11ll1ll_opy_ (u"ࠩࡳࡽࡹ࡮࡯࡯ࠩὃ"),
                bstack11ll1ll_opy_ (u"ࠪࡧࡴࡪࡥࠨὄ"): self.code
            },
            bstack11ll1ll_opy_ (u"ࠫࡸࡩ࡯ࡱࡧࡶࠫὅ"): self.scope,
            bstack11ll1ll_opy_ (u"ࠬࡺࡡࡨࡵࠪ὆"): self.tags,
            bstack11ll1ll_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩ὇"): self.framework,
            bstack11ll1ll_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫὈ"): self.started_at
        }
    def bstack111111l111l_opy_(self):
        return {
         bstack11ll1ll_opy_ (u"ࠨ࡯ࡨࡸࡦ࠭Ὁ"): self.meta
        }
    def bstack11111111lll_opy_(self):
        return {
            bstack11ll1ll_opy_ (u"ࠩࡦࡹࡸࡺ࡯࡮ࡔࡨࡶࡺࡴࡐࡢࡴࡤࡱࠬὊ"): {
                bstack11ll1ll_opy_ (u"ࠪࡶࡪࡸࡵ࡯ࡡࡱࡥࡲ࡫ࠧὋ"): self.bstack111111l1l11_opy_
            }
        }
    def bstack111111l1ll1_opy_(self, bstack111111l1111_opy_, details):
        step = next(filter(lambda st: st[bstack11ll1ll_opy_ (u"ࠫ࡮ࡪࠧὌ")] == bstack111111l1111_opy_, self.meta[bstack11ll1ll_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫὍ")]), None)
        step.update(details)
    def bstack11l1l1ll_opy_(self, bstack111111l1111_opy_):
        step = next(filter(lambda st: st[bstack11ll1ll_opy_ (u"࠭ࡩࡥࠩ὎")] == bstack111111l1111_opy_, self.meta[bstack11ll1ll_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭὏")]), None)
        step.update({
            bstack11ll1ll_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬὐ"): bstack1ll111ll_opy_()
        })
    def bstack1ll111l1_opy_(self, bstack111111l1111_opy_, result, duration=None):
        bstack1ll11ll1lll_opy_ = bstack1ll111ll_opy_()
        if bstack111111l1111_opy_ is not None and self.meta.get(bstack11ll1ll_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨὑ")):
            step = next(filter(lambda st: st[bstack11ll1ll_opy_ (u"ࠪ࡭ࡩ࠭ὒ")] == bstack111111l1111_opy_, self.meta[bstack11ll1ll_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪὓ")]), None)
            step.update({
                bstack11ll1ll_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪὔ"): bstack1ll11ll1lll_opy_,
                bstack11ll1ll_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࠨὕ"): duration if duration else bstack111l1l11ll1_opy_(step[bstack11ll1ll_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫὖ")], bstack1ll11ll1lll_opy_),
                bstack11ll1ll_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨὗ"): result.result,
                bstack11ll1ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡵࡳࡧࠪ὘"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack1111111l11l_opy_):
        if self.meta.get(bstack11ll1ll_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩὙ")):
            self.meta[bstack11ll1ll_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪ὚")].append(bstack1111111l11l_opy_)
        else:
            self.meta[bstack11ll1ll_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫὛ")] = [ bstack1111111l11l_opy_ ]
    def bstack111111l11ll_opy_(self):
        return {
            bstack11ll1ll_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ὜"): self.bstack1ll11111_opy_(),
            **self.bstack1111111l1l1_opy_(),
            **self.bstack1111111l111_opy_(),
            **self.bstack111111l111l_opy_()
        }
    def bstack1111111ll11_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack11ll1ll_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬὝ"): self.bstack1ll11ll1lll_opy_,
            bstack11ll1ll_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࡢ࡭ࡳࡥ࡭ࡴࠩ὞"): self.duration,
            bstack11ll1ll_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩὟ"): self.result.result
        }
        if data[bstack11ll1ll_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪὠ")] == bstack11ll1ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫὡ"):
            data[bstack11ll1ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪࡥࡴࡺࡲࡨࠫὢ")] = self.result.bstack1111111l11_opy_()
            data[bstack11ll1ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫ࠧὣ")] = [{bstack11ll1ll_opy_ (u"ࠧࡣࡣࡦ࡯ࡹࡸࡡࡤࡧࠪὤ"): self.result.bstack1111l111111_opy_()}]
        return data
    def bstack111111l11l1_opy_(self):
        return {
            bstack11ll1ll_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭ὥ"): self.bstack1ll11111_opy_(),
            **self.bstack1111111l1l1_opy_(),
            **self.bstack1111111l111_opy_(),
            **self.bstack1111111ll11_opy_(),
            **self.bstack111111l111l_opy_()
        }
    def bstack1ll1lll1_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack11ll1ll_opy_ (u"ࠩࡖࡸࡦࡸࡴࡦࡦࠪὦ") in event:
            return self.bstack111111l11ll_opy_()
        elif bstack11ll1ll_opy_ (u"ࠪࡊ࡮ࡴࡩࡴࡪࡨࡨࠬὧ") in event:
            return self.bstack111111l11l1_opy_()
    def event_key(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1ll11ll1lll_opy_ = time if time else bstack1ll111ll_opy_()
        self.duration = duration if duration else bstack111l1l11ll1_opy_(self.started_at, self.bstack1ll11ll1lll_opy_)
        if result:
            self.result = result
class bstack1l1ll1ll_opy_(bstack1ll11l1l_opy_):
    def __init__(self, hooks=[], bstack1l1l11ll_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack1l1l11ll_opy_ = bstack1l1l11ll_opy_
        super().__init__(*args, **kwargs, bstack11l1l1ll11_opy_=bstack11ll1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࠩὨ"))
    @classmethod
    def bstack1111111ll1l_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack11ll1ll_opy_ (u"ࠬ࡯ࡤࠨὩ"): id(step),
                bstack11ll1ll_opy_ (u"࠭ࡴࡦࡺࡷࠫὪ"): step.name,
                bstack11ll1ll_opy_ (u"ࠧ࡬ࡧࡼࡻࡴࡸࡤࠨὫ"): step.keyword,
            })
        return bstack1l1ll1ll_opy_(
            **kwargs,
            meta={
                bstack11ll1ll_opy_ (u"ࠨࡨࡨࡥࡹࡻࡲࡦࠩὬ"): {
                    bstack11ll1ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧὭ"): feature.name,
                    bstack11ll1ll_opy_ (u"ࠪࡴࡦࡺࡨࠨὮ"): feature.filename,
                    bstack11ll1ll_opy_ (u"ࠫࡩ࡫ࡳࡤࡴ࡬ࡴࡹ࡯࡯࡯ࠩὯ"): feature.description
                },
                bstack11ll1ll_opy_ (u"ࠬࡹࡣࡦࡰࡤࡶ࡮ࡵࠧὰ"): {
                    bstack11ll1ll_opy_ (u"࠭࡮ࡢ࡯ࡨࠫά"): scenario.name
                },
                bstack11ll1ll_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ὲ"): steps,
                bstack11ll1ll_opy_ (u"ࠨࡧࡻࡥࡲࡶ࡬ࡦࡵࠪέ"): bstack11l111l1111_opy_(test)
            }
        )
    def bstack111111l1l1l_opy_(self):
        return {
            bstack11ll1ll_opy_ (u"ࠩ࡫ࡳࡴࡱࡳࠨὴ"): self.hooks
        }
    def bstack1111111llll_opy_(self):
        if self.bstack1l1l11ll_opy_:
            return {
                bstack11ll1ll_opy_ (u"ࠪ࡭ࡳࡺࡥࡨࡴࡤࡸ࡮ࡵ࡮ࡴࠩή"): self.bstack1l1l11ll_opy_
            }
        return {}
    def bstack111111l11l1_opy_(self):
        return {
            **super().bstack111111l11l1_opy_(),
            **self.bstack111111l1l1l_opy_()
        }
    def bstack111111l11ll_opy_(self):
        return {
            **super().bstack111111l11ll_opy_(),
            **self.bstack1111111llll_opy_()
        }
    def event_key(self):
        return bstack11ll1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡡࡵࡹࡳ࠭ὶ")
class bstack1llll111_opy_(bstack1ll11l1l_opy_):
    def __init__(self, hook_type, *args,bstack1l1l11ll_opy_={}, **kwargs):
        self.hook_type = hook_type
        self.bstack1l1111l1ll1_opy_ = None
        self.bstack1l1l11ll_opy_ = bstack1l1l11ll_opy_
        super().__init__(*args, **kwargs, bstack11l1l1ll11_opy_=bstack11ll1ll_opy_ (u"ࠬ࡮࡯ࡰ࡭ࠪί"))
    def bstack1l1lll11_opy_(self):
        return self.hook_type
    def bstack1111111l1ll_opy_(self):
        return {
            bstack11ll1ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡹࡿࡰࡦࠩὸ"): self.hook_type
        }
    def bstack111111l11l1_opy_(self):
        return {
            **super().bstack111111l11l1_opy_(),
            **self.bstack1111111l1ll_opy_()
        }
    def bstack111111l11ll_opy_(self):
        return {
            **super().bstack111111l11ll_opy_(),
            bstack11ll1ll_opy_ (u"ࠧࡵࡧࡶࡸࡤࡸࡵ࡯ࡡ࡬ࡨࠬό"): self.bstack1l1111l1ll1_opy_,
            **self.bstack1111111l1ll_opy_()
        }
    def event_key(self):
        return bstack11ll1ll_opy_ (u"ࠨࡪࡲࡳࡰࡥࡲࡶࡰࠪὺ")
    def bstack11l1l1l1_opy_(self, bstack1l1111l1ll1_opy_):
        self.bstack1l1111l1ll1_opy_ = bstack1l1111l1ll1_opy_