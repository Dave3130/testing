# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
import os
from uuid import uuid4
from bstack_utils.helper import bstack1ll1ll1l_opy_, bstack1111l1111ll_opy_
from bstack_utils.bstack111ll11ll1_opy_ import bstack11l1111ll1l_opy_
class bstack1l1lll11_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, started_at=None, framework=None, tags=[], scope=[], bstack111111l1ll1_opy_=None, bstack111111ll1l1_opy_=True, bstack1ll1111l11l_opy_=None, bstack1l11l1111l_opy_=None, result=None, duration=None, bstack11lll1ll_opy_=None, meta={}):
        self.bstack11lll1ll_opy_ = bstack11lll1ll_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack111111ll1l1_opy_:
            self.uuid = uuid4().__str__()
        self.started_at = started_at
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack111111l1ll1_opy_ = bstack111111l1ll1_opy_
        self.bstack1ll1111l11l_opy_ = bstack1ll1111l11l_opy_
        self.bstack1l11l1111l_opy_ = bstack1l11l1111l_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
        self.hooks = []
    def bstack1l1ll111_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack11l1111l_opy_(self, meta):
        self.meta = meta
    def bstack11l1l11l_opy_(self, hooks):
        self.hooks = hooks
    def bstack111111lll11_opy_(self):
        bstack111111l11l1_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack11l11ll_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪἥ"): bstack111111l11l1_opy_,
            bstack11l11ll_opy_ (u"ࠨ࡮ࡲࡧࡦࡺࡩࡰࡰࠪἦ"): bstack111111l11l1_opy_,
            bstack11l11ll_opy_ (u"ࠩࡹࡧࡤ࡬ࡩ࡭ࡧࡳࡥࡹ࡮ࠧἧ"): bstack111111l11l1_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack11l11ll_opy_ (u"࡙ࠥࡳ࡫ࡸࡱࡧࡦࡸࡪࡪࠠࡢࡴࡪࡹࡲ࡫࡮ࡵ࠼ࠣࠦἨ") + key)
            setattr(self, key, val)
    def bstack111111l1lll_opy_(self):
        return {
            bstack11l11ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩἩ"): self.name,
            bstack11l11ll_opy_ (u"ࠬࡨ࡯ࡥࡻࠪἪ"): {
                bstack11l11ll_opy_ (u"࠭࡬ࡢࡰࡪࠫἫ"): bstack11l11ll_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧἬ"),
                bstack11l11ll_opy_ (u"ࠨࡥࡲࡨࡪ࠭Ἥ"): self.code
            },
            bstack11l11ll_opy_ (u"ࠩࡶࡧࡴࡶࡥࡴࠩἮ"): self.scope,
            bstack11l11ll_opy_ (u"ࠪࡸࡦ࡭ࡳࠨἯ"): self.tags,
            bstack11l11ll_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧἰ"): self.framework,
            bstack11l11ll_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩἱ"): self.started_at
        }
    def bstack111111ll11l_opy_(self):
        return {
         bstack11l11ll_opy_ (u"࠭࡭ࡦࡶࡤࠫἲ"): self.meta
        }
    def bstack111111l1111_opy_(self):
        return {
            bstack11l11ll_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡒࡦࡴࡸࡲࡕࡧࡲࡢ࡯ࠪἳ"): {
                bstack11l11ll_opy_ (u"ࠨࡴࡨࡶࡺࡴ࡟࡯ࡣࡰࡩࠬἴ"): self.bstack111111l1ll1_opy_
            }
        }
    def bstack111111ll111_opy_(self, bstack1111111lll1_opy_, details):
        step = next(filter(lambda st: st[bstack11l11ll_opy_ (u"ࠩ࡬ࡨࠬἵ")] == bstack1111111lll1_opy_, self.meta[bstack11l11ll_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩἶ")]), None)
        step.update(details)
    def bstack11l1l1l1_opy_(self, bstack1111111lll1_opy_):
        step = next(filter(lambda st: st[bstack11l11ll_opy_ (u"ࠫ࡮ࡪࠧἷ")] == bstack1111111lll1_opy_, self.meta[bstack11l11ll_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫἸ")]), None)
        step.update({
            bstack11l11ll_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪἹ"): bstack1ll1ll1l_opy_()
        })
    def bstack1l11llll_opy_(self, bstack1111111lll1_opy_, result, duration=None):
        bstack1ll1111l11l_opy_ = bstack1ll1ll1l_opy_()
        if bstack1111111lll1_opy_ is not None and self.meta.get(bstack11l11ll_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭Ἲ")):
            step = next(filter(lambda st: st[bstack11l11ll_opy_ (u"ࠨ࡫ࡧࠫἻ")] == bstack1111111lll1_opy_, self.meta[bstack11l11ll_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨἼ")]), None)
            step.update({
                bstack11l11ll_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨἽ"): bstack1ll1111l11l_opy_,
                bstack11l11ll_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭Ἶ"): duration if duration else bstack1111l1111ll_opy_(step[bstack11l11ll_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩἿ")], bstack1ll1111l11l_opy_),
                bstack11l11ll_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ὀ"): result.result,
                bstack11l11ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨὁ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack1111111llll_opy_):
        if self.meta.get(bstack11l11ll_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧὂ")):
            self.meta[bstack11l11ll_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨὃ")].append(bstack1111111llll_opy_)
        else:
            self.meta[bstack11l11ll_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩὄ")] = [ bstack1111111llll_opy_ ]
    def bstack111111ll1ll_opy_(self):
        return {
            bstack11l11ll_opy_ (u"ࠫࡺࡻࡩࡥࠩὅ"): self.bstack1l1ll111_opy_(),
            **self.bstack111111l1lll_opy_(),
            **self.bstack111111lll11_opy_(),
            **self.bstack111111ll11l_opy_()
        }
    def bstack111111l1l11_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack11l11ll_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪ὆"): self.bstack1ll1111l11l_opy_,
            bstack11l11ll_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡣࡲࡹࠧ὇"): self.duration,
            bstack11l11ll_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧὈ"): self.result.result
        }
        if data[bstack11l11ll_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨὉ")] == bstack11l11ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩὊ"):
            data[bstack11l11ll_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠩὋ")] = self.result.bstack11111111ll_opy_()
            data[bstack11l11ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬὌ")] = [{bstack11l11ll_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨὍ"): self.result.bstack1111l111lll_opy_()}]
        return data
    def bstack111111l11ll_opy_(self):
        return {
            bstack11l11ll_opy_ (u"࠭ࡵࡶ࡫ࡧࠫ὎"): self.bstack1l1ll111_opy_(),
            **self.bstack111111l1lll_opy_(),
            **self.bstack111111lll11_opy_(),
            **self.bstack111111l1l11_opy_(),
            **self.bstack111111ll11l_opy_()
        }
    def bstack1ll11lll_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack11l11ll_opy_ (u"ࠧࡔࡶࡤࡶࡹ࡫ࡤࠨ὏") in event:
            return self.bstack111111ll1ll_opy_()
        elif bstack11l11ll_opy_ (u"ࠨࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪὐ") in event:
            return self.bstack111111l11ll_opy_()
    def event_key(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1ll1111l11l_opy_ = time if time else bstack1ll1ll1l_opy_()
        self.duration = duration if duration else bstack1111l1111ll_opy_(self.started_at, self.bstack1ll1111l11l_opy_)
        if result:
            self.result = result
class bstack1l11l1ll_opy_(bstack1l1lll11_opy_):
    def __init__(self, hooks=[], bstack1llll1ll_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack1llll1ll_opy_ = bstack1llll1ll_opy_
        super().__init__(*args, **kwargs, bstack1l11l1111l_opy_=bstack11l11ll_opy_ (u"ࠩࡷࡩࡸࡺࠧὑ"))
    @classmethod
    def bstack111111l111l_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack11l11ll_opy_ (u"ࠪ࡭ࡩ࠭ὒ"): id(step),
                bstack11l11ll_opy_ (u"ࠫࡹ࡫ࡸࡵࠩὓ"): step.name,
                bstack11l11ll_opy_ (u"ࠬࡱࡥࡺࡹࡲࡶࡩ࠭ὔ"): step.keyword,
            })
        return bstack1l11l1ll_opy_(
            **kwargs,
            meta={
                bstack11l11ll_opy_ (u"࠭ࡦࡦࡣࡷࡹࡷ࡫ࠧὕ"): {
                    bstack11l11ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬὖ"): feature.name,
                    bstack11l11ll_opy_ (u"ࠨࡲࡤࡸ࡭࠭ὗ"): feature.filename,
                    bstack11l11ll_opy_ (u"ࠩࡧࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧ὘"): feature.description
                },
                bstack11l11ll_opy_ (u"ࠪࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬὙ"): {
                    bstack11l11ll_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ὚"): scenario.name
                },
                bstack11l11ll_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫὛ"): steps,
                bstack11l11ll_opy_ (u"࠭ࡥࡹࡣࡰࡴࡱ࡫ࡳࠨ὜"): bstack11l1111ll1l_opy_(test)
            }
        )
    def bstack1111111ll11_opy_(self):
        return {
            bstack11l11ll_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭Ὕ"): self.hooks
        }
    def bstack111111l1l1l_opy_(self):
        if self.bstack1llll1ll_opy_:
            return {
                bstack11l11ll_opy_ (u"ࠨ࡫ࡱࡸࡪ࡭ࡲࡢࡶ࡬ࡳࡳࡹࠧ὞"): self.bstack1llll1ll_opy_
            }
        return {}
    def bstack111111l11ll_opy_(self):
        return {
            **super().bstack111111l11ll_opy_(),
            **self.bstack1111111ll11_opy_()
        }
    def bstack111111ll1ll_opy_(self):
        return {
            **super().bstack111111ll1ll_opy_(),
            **self.bstack111111l1l1l_opy_()
        }
    def event_key(self):
        return bstack11l11ll_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫὟ")
class bstack1l1l1ll1_opy_(bstack1l1lll11_opy_):
    def __init__(self, hook_type, *args,bstack1llll1ll_opy_={}, **kwargs):
        self.hook_type = hook_type
        self.bstack1l11111l11l_opy_ = None
        self.bstack1llll1ll_opy_ = bstack1llll1ll_opy_
        super().__init__(*args, **kwargs, bstack1l11l1111l_opy_=bstack11l11ll_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨὠ"))
    def bstack1lll111l_opy_(self):
        return self.hook_type
    def bstack1111111ll1l_opy_(self):
        return {
            bstack11l11ll_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧὡ"): self.hook_type
        }
    def bstack111111l11ll_opy_(self):
        return {
            **super().bstack111111l11ll_opy_(),
            **self.bstack1111111ll1l_opy_()
        }
    def bstack111111ll1ll_opy_(self):
        return {
            **super().bstack111111ll1ll_opy_(),
            bstack11l11ll_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡪࡦࠪὢ"): self.bstack1l11111l11l_opy_,
            **self.bstack1111111ll1l_opy_()
        }
    def event_key(self):
        return bstack11l11ll_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࠨὣ")
    def bstack11l11l1l_opy_(self, bstack1l11111l11l_opy_):
        self.bstack1l11111l11l_opy_ = bstack1l11111l11l_opy_