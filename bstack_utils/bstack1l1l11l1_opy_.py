# coding: UTF-8
import sys
bstack1l1l111_opy_ = sys.version_info [0] == 2
bstack11l1ll_opy_ = 2048
bstack1llll11_opy_ = 7
def bstack11ll1l_opy_ (bstack1llllll1_opy_):
    global bstack1ll11_opy_
    bstack11ll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1lll111_opy_ = bstack1llllll1_opy_ [:-1]
    bstack11l11l_opy_ = bstack11ll111_opy_ % len (bstack1lll111_opy_)
    bstack1l1ll11_opy_ = bstack1lll111_opy_ [:bstack11l11l_opy_] + bstack1lll111_opy_ [bstack11l11l_opy_:]
    if bstack1l1l111_opy_:
        bstack11111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    else:
        bstack11111l1_opy_ = str () .join ([chr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    return eval (bstack11111l1_opy_)
import os
from uuid import uuid4
from bstack_utils.helper import bstack1l111ll1_opy_, bstack111l1l11111_opy_
from bstack_utils.bstack111ll1l1ll_opy_ import bstack11l111l111l_opy_
class bstack1ll1ll11_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, started_at=None, framework=None, tags=[], scope=[], bstack111111l11ll_opy_=None, bstack111111l11l1_opy_=True, bstack1ll111l1111_opy_=None, bstack1ll1ll1l11_opy_=None, result=None, duration=None, bstack1l11l1ll_opy_=None, meta={}):
        self.bstack1l11l1ll_opy_ = bstack1l11l1ll_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack111111l11l1_opy_:
            self.uuid = uuid4().__str__()
        self.started_at = started_at
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack111111l11ll_opy_ = bstack111111l11ll_opy_
        self.bstack1ll111l1111_opy_ = bstack1ll111l1111_opy_
        self.bstack1ll1ll1l11_opy_ = bstack1ll1ll1l11_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
        self.hooks = []
    def bstack1l11l1l1_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack11l1l1l1_opy_(self, meta):
        self.meta = meta
    def bstack11l11l11_opy_(self, hooks):
        self.hooks = hooks
    def bstack1111111llll_opy_(self):
        bstack111111l1l11_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack11ll1l_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫἦ"): bstack111111l1l11_opy_,
            bstack11ll1l_opy_ (u"ࠩ࡯ࡳࡨࡧࡴࡪࡱࡱࠫἧ"): bstack111111l1l11_opy_,
            bstack11ll1l_opy_ (u"ࠪࡺࡨࡥࡦࡪ࡮ࡨࡴࡦࡺࡨࠨἨ"): bstack111111l1l11_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack11ll1l_opy_ (u"࡚ࠦࡴࡥࡹࡲࡨࡧࡹ࡫ࡤࠡࡣࡵ࡫ࡺࡳࡥ࡯ࡶ࠽ࠤࠧἩ") + key)
            setattr(self, key, val)
    def bstack111111l1ll1_opy_(self):
        return {
            bstack11ll1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪἪ"): self.name,
            bstack11ll1l_opy_ (u"࠭ࡢࡰࡦࡼࠫἫ"): {
                bstack11ll1l_opy_ (u"ࠧ࡭ࡣࡱ࡫ࠬἬ"): bstack11ll1l_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨἭ"),
                bstack11ll1l_opy_ (u"ࠩࡦࡳࡩ࡫ࠧἮ"): self.code
            },
            bstack11ll1l_opy_ (u"ࠪࡷࡨࡵࡰࡦࡵࠪἯ"): self.scope,
            bstack11ll1l_opy_ (u"ࠫࡹࡧࡧࡴࠩἰ"): self.tags,
            bstack11ll1l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨἱ"): self.framework,
            bstack11ll1l_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪἲ"): self.started_at
        }
    def bstack1111111ll11_opy_(self):
        return {
         bstack11ll1l_opy_ (u"ࠧ࡮ࡧࡷࡥࠬἳ"): self.meta
        }
    def bstack111111lll11_opy_(self):
        return {
            bstack11ll1l_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡓࡧࡵࡹࡳࡖࡡࡳࡣࡰࠫἴ"): {
                bstack11ll1l_opy_ (u"ࠩࡵࡩࡷࡻ࡮ࡠࡰࡤࡱࡪ࠭ἵ"): self.bstack111111l11ll_opy_
            }
        }
    def bstack111111ll1l1_opy_(self, bstack111111l1111_opy_, details):
        step = next(filter(lambda st: st[bstack11ll1l_opy_ (u"ࠪ࡭ࡩ࠭ἶ")] == bstack111111l1111_opy_, self.meta[bstack11ll1l_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪἷ")]), None)
        step.update(details)
    def bstack11l1l11l_opy_(self, bstack111111l1111_opy_):
        step = next(filter(lambda st: st[bstack11ll1l_opy_ (u"ࠬ࡯ࡤࠨἸ")] == bstack111111l1111_opy_, self.meta[bstack11ll1l_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬἹ")]), None)
        step.update({
            bstack11ll1l_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫἺ"): bstack1l111ll1_opy_()
        })
    def bstack1l1l11ll_opy_(self, bstack111111l1111_opy_, result, duration=None):
        bstack1ll111l1111_opy_ = bstack1l111ll1_opy_()
        if bstack111111l1111_opy_ is not None and self.meta.get(bstack11ll1l_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧἻ")):
            step = next(filter(lambda st: st[bstack11ll1l_opy_ (u"ࠩ࡬ࡨࠬἼ")] == bstack111111l1111_opy_, self.meta[bstack11ll1l_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩἽ")]), None)
            step.update({
                bstack11ll1l_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩἾ"): bstack1ll111l1111_opy_,
                bstack11ll1l_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧἿ"): duration if duration else bstack111l1l11111_opy_(step[bstack11ll1l_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪὀ")], bstack1ll111l1111_opy_),
                bstack11ll1l_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧὁ"): result.result,
                bstack11ll1l_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩὂ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack111111l1l1l_opy_):
        if self.meta.get(bstack11ll1l_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨὃ")):
            self.meta[bstack11ll1l_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩὄ")].append(bstack111111l1l1l_opy_)
        else:
            self.meta[bstack11ll1l_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪὅ")] = [ bstack111111l1l1l_opy_ ]
    def bstack111111l111l_opy_(self):
        return {
            bstack11ll1l_opy_ (u"ࠬࡻࡵࡪࡦࠪ὆"): self.bstack1l11l1l1_opy_(),
            **self.bstack111111l1ll1_opy_(),
            **self.bstack1111111llll_opy_(),
            **self.bstack1111111ll11_opy_()
        }
    def bstack1111111lll1_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack11ll1l_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ὇"): self.bstack1ll111l1111_opy_,
            bstack11ll1l_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡤࡳࡳࠨὈ"): self.duration,
            bstack11ll1l_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨὉ"): self.result.result
        }
        if data[bstack11ll1l_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩὊ")] == bstack11ll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪὋ"):
            data[bstack11ll1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠪὌ")] = self.result.bstack11111111ll_opy_()
            data[bstack11ll1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭Ὅ")] = [{bstack11ll1l_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩ὎"): self.result.bstack111l1l1111l_opy_()}]
        return data
    def bstack111111ll1ll_opy_(self):
        return {
            bstack11ll1l_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ὏"): self.bstack1l11l1l1_opy_(),
            **self.bstack111111l1ll1_opy_(),
            **self.bstack1111111llll_opy_(),
            **self.bstack1111111lll1_opy_(),
            **self.bstack1111111ll11_opy_()
        }
    def bstack11llllll_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack11ll1l_opy_ (u"ࠨࡕࡷࡥࡷࡺࡥࡥࠩὐ") in event:
            return self.bstack111111l111l_opy_()
        elif bstack11ll1l_opy_ (u"ࠩࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫὑ") in event:
            return self.bstack111111ll1ll_opy_()
    def event_key(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1ll111l1111_opy_ = time if time else bstack1l111ll1_opy_()
        self.duration = duration if duration else bstack111l1l11111_opy_(self.started_at, self.bstack1ll111l1111_opy_)
        if result:
            self.result = result
class bstack1l1l1l11_opy_(bstack1ll1ll11_opy_):
    def __init__(self, hooks=[], bstack11lllll1_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack11lllll1_opy_ = bstack11lllll1_opy_
        super().__init__(*args, **kwargs, bstack1ll1ll1l11_opy_=bstack11ll1l_opy_ (u"ࠪࡸࡪࡹࡴࠨὒ"))
    @classmethod
    def bstack1111111ll1l_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack11ll1l_opy_ (u"ࠫ࡮ࡪࠧὓ"): id(step),
                bstack11ll1l_opy_ (u"ࠬࡺࡥࡹࡶࠪὔ"): step.name,
                bstack11ll1l_opy_ (u"࠭࡫ࡦࡻࡺࡳࡷࡪࠧὕ"): step.keyword,
            })
        return bstack1l1l1l11_opy_(
            **kwargs,
            meta={
                bstack11ll1l_opy_ (u"ࠧࡧࡧࡤࡸࡺࡸࡥࠨὖ"): {
                    bstack11ll1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ὗ"): feature.name,
                    bstack11ll1l_opy_ (u"ࠩࡳࡥࡹ࡮ࠧ὘"): feature.filename,
                    bstack11ll1l_opy_ (u"ࠪࡨࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠨὙ"): feature.description
                },
                bstack11ll1l_opy_ (u"ࠫࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭὚"): {
                    bstack11ll1l_opy_ (u"ࠬࡴࡡ࡮ࡧࠪὛ"): scenario.name
                },
                bstack11ll1l_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬ὜"): steps,
                bstack11ll1l_opy_ (u"ࠧࡦࡺࡤࡱࡵࡲࡥࡴࠩὝ"): bstack11l111l111l_opy_(test)
            }
        )
    def bstack111111ll11l_opy_(self):
        return {
            bstack11ll1l_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧ὞"): self.hooks
        }
    def bstack111111ll111_opy_(self):
        if self.bstack11lllll1_opy_:
            return {
                bstack11ll1l_opy_ (u"ࠩ࡬ࡲࡹ࡫ࡧࡳࡣࡷ࡭ࡴࡴࡳࠨὟ"): self.bstack11lllll1_opy_
            }
        return {}
    def bstack111111ll1ll_opy_(self):
        return {
            **super().bstack111111ll1ll_opy_(),
            **self.bstack111111ll11l_opy_()
        }
    def bstack111111l111l_opy_(self):
        return {
            **super().bstack111111l111l_opy_(),
            **self.bstack111111ll111_opy_()
        }
    def event_key(self):
        return bstack11ll1l_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࠬὠ")
class bstack1l11l111_opy_(bstack1ll1ll11_opy_):
    def __init__(self, hook_type, *args,bstack11lllll1_opy_={}, **kwargs):
        self.hook_type = hook_type
        self.bstack1l111l111ll_opy_ = None
        self.bstack11lllll1_opy_ = bstack11lllll1_opy_
        super().__init__(*args, **kwargs, bstack1ll1ll1l11_opy_=bstack11ll1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩὡ"))
    def bstack11llll1l_opy_(self):
        return self.hook_type
    def bstack111111l1lll_opy_(self):
        return {
            bstack11ll1l_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨὢ"): self.hook_type
        }
    def bstack111111ll1ll_opy_(self):
        return {
            **super().bstack111111ll1ll_opy_(),
            **self.bstack111111l1lll_opy_()
        }
    def bstack111111l111l_opy_(self):
        return {
            **super().bstack111111l111l_opy_(),
            bstack11ll1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠ࡫ࡧࠫὣ"): self.bstack1l111l111ll_opy_,
            **self.bstack111111l1lll_opy_()
        }
    def event_key(self):
        return bstack11ll1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࠩὤ")
    def bstack11l11l1l_opy_(self, bstack1l111l111ll_opy_):
        self.bstack1l111l111ll_opy_ = bstack1l111l111ll_opy_