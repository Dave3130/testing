# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
import os
from uuid import uuid4
from bstack_utils.helper import bstack1l111lll_opy_, bstack111l1l1l11l_opy_
from bstack_utils.bstack1ll1l1l11l_opy_ import bstack11l111l11l1_opy_
class bstack11lllll1_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, started_at=None, framework=None, tags=[], scope=[], bstack111111ll1ll_opy_=None, bstack111111l1l11_opy_=True, bstack1ll111lll11_opy_=None, bstack11111l11ll_opy_=None, result=None, duration=None, bstack1ll1lll1_opy_=None, meta={}):
        self.bstack1ll1lll1_opy_ = bstack1ll1lll1_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack111111l1l11_opy_:
            self.uuid = uuid4().__str__()
        self.started_at = started_at
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack111111ll1ll_opy_ = bstack111111ll1ll_opy_
        self.bstack1ll111lll11_opy_ = bstack1ll111lll11_opy_
        self.bstack11111l11ll_opy_ = bstack11111l11ll_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
        self.hooks = []
    def bstack1l1111l1_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack11l1l11l_opy_(self, meta):
        self.meta = meta
    def bstack11l11lll_opy_(self, hooks):
        self.hooks = hooks
    def bstack111111l1ll1_opy_(self):
        bstack111111ll1l1_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack1lll11l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭ἡ"): bstack111111ll1l1_opy_,
            bstack1lll11l_opy_ (u"ࠫࡱࡵࡣࡢࡶ࡬ࡳࡳ࠭ἢ"): bstack111111ll1l1_opy_,
            bstack1lll11l_opy_ (u"ࠬࡼࡣࡠࡨ࡬ࡰࡪࡶࡡࡵࡪࠪἣ"): bstack111111ll1l1_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack1lll11l_opy_ (u"ࠨࡕ࡯ࡧࡻࡴࡪࡩࡴࡦࡦࠣࡥࡷ࡭ࡵ࡮ࡧࡱࡸ࠿ࠦࠢἤ") + key)
            setattr(self, key, val)
    def bstack111111l1l1l_opy_(self):
        return {
            bstack1lll11l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬἥ"): self.name,
            bstack1lll11l_opy_ (u"ࠨࡤࡲࡨࡾ࠭ἦ"): {
                bstack1lll11l_opy_ (u"ࠩ࡯ࡥࡳ࡭ࠧἧ"): bstack1lll11l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪἨ"),
                bstack1lll11l_opy_ (u"ࠫࡨࡵࡤࡦࠩἩ"): self.code
            },
            bstack1lll11l_opy_ (u"ࠬࡹࡣࡰࡲࡨࡷࠬἪ"): self.scope,
            bstack1lll11l_opy_ (u"࠭ࡴࡢࡩࡶࠫἫ"): self.tags,
            bstack1lll11l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪἬ"): self.framework,
            bstack1lll11l_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬἭ"): self.started_at
        }
    def bstack111111l111l_opy_(self):
        return {
         bstack1lll11l_opy_ (u"ࠩࡰࡩࡹࡧࠧἮ"): self.meta
        }
    def bstack1111111lll1_opy_(self):
        return {
            bstack1lll11l_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡕࡩࡷࡻ࡮ࡑࡣࡵࡥࡲ࠭Ἧ"): {
                bstack1lll11l_opy_ (u"ࠫࡷ࡫ࡲࡶࡰࡢࡲࡦࡳࡥࠨἰ"): self.bstack111111ll1ll_opy_
            }
        }
    def bstack111111l11l1_opy_(self, bstack1111111l1ll_opy_, details):
        step = next(filter(lambda st: st[bstack1lll11l_opy_ (u"ࠬ࡯ࡤࠨἱ")] == bstack1111111l1ll_opy_, self.meta[bstack1lll11l_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬἲ")]), None)
        step.update(details)
    def bstack11l1l1ll_opy_(self, bstack1111111l1ll_opy_):
        step = next(filter(lambda st: st[bstack1lll11l_opy_ (u"ࠧࡪࡦࠪἳ")] == bstack1111111l1ll_opy_, self.meta[bstack1lll11l_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧἴ")]), None)
        step.update({
            bstack1lll11l_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ἵ"): bstack1l111lll_opy_()
        })
    def bstack1l1l1ll1_opy_(self, bstack1111111l1ll_opy_, result, duration=None):
        bstack1ll111lll11_opy_ = bstack1l111lll_opy_()
        if bstack1111111l1ll_opy_ is not None and self.meta.get(bstack1lll11l_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩἶ")):
            step = next(filter(lambda st: st[bstack1lll11l_opy_ (u"ࠫ࡮ࡪࠧἷ")] == bstack1111111l1ll_opy_, self.meta[bstack1lll11l_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫἸ")]), None)
            step.update({
                bstack1lll11l_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫἹ"): bstack1ll111lll11_opy_,
                bstack1lll11l_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࠩἺ"): duration if duration else bstack111l1l1l11l_opy_(step[bstack1lll11l_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬἻ")], bstack1ll111lll11_opy_),
                bstack1lll11l_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩἼ"): result.result,
                bstack1lll11l_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫἽ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack1111111ll1l_opy_):
        if self.meta.get(bstack1lll11l_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪἾ")):
            self.meta[bstack1lll11l_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫἿ")].append(bstack1111111ll1l_opy_)
        else:
            self.meta[bstack1lll11l_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬὀ")] = [ bstack1111111ll1l_opy_ ]
    def bstack111111l1lll_opy_(self):
        return {
            bstack1lll11l_opy_ (u"ࠧࡶࡷ࡬ࡨࠬὁ"): self.bstack1l1111l1_opy_(),
            **self.bstack111111l1l1l_opy_(),
            **self.bstack111111l1ll1_opy_(),
            **self.bstack111111l111l_opy_()
        }
    def bstack111111l1111_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack1lll11l_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ὂ"): self.bstack1ll111lll11_opy_,
            bstack1lll11l_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࡣ࡮ࡴ࡟࡮ࡵࠪὃ"): self.duration,
            bstack1lll11l_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪὄ"): self.result.result
        }
        if data[bstack1lll11l_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫὅ")] == bstack1lll11l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ὆"):
            data[bstack1lll11l_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫࡟ࡵࡻࡳࡩࠬ὇")] = self.result.bstack1111111lll_opy_()
            data[bstack1lll11l_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨὈ")] = [{bstack1lll11l_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫὉ"): self.result.bstack1111lllll11_opy_()}]
        return data
    def bstack111111ll111_opy_(self):
        return {
            bstack1lll11l_opy_ (u"ࠩࡸࡹ࡮ࡪࠧὊ"): self.bstack1l1111l1_opy_(),
            **self.bstack111111l1l1l_opy_(),
            **self.bstack111111l1ll1_opy_(),
            **self.bstack111111l1111_opy_(),
            **self.bstack111111l111l_opy_()
        }
    def bstack1l11l1l1_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack1lll11l_opy_ (u"ࠪࡗࡹࡧࡲࡵࡧࡧࠫὋ") in event:
            return self.bstack111111l1lll_opy_()
        elif bstack1lll11l_opy_ (u"ࠫࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭Ὄ") in event:
            return self.bstack111111ll111_opy_()
    def event_key(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1ll111lll11_opy_ = time if time else bstack1l111lll_opy_()
        self.duration = duration if duration else bstack111l1l1l11l_opy_(self.started_at, self.bstack1ll111lll11_opy_)
        if result:
            self.result = result
class bstack11llllll_opy_(bstack11lllll1_opy_):
    def __init__(self, hooks=[], bstack1l1l11l1_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack1l1l11l1_opy_ = bstack1l1l11l1_opy_
        super().__init__(*args, **kwargs, bstack11111l11ll_opy_=bstack1lll11l_opy_ (u"ࠬࡺࡥࡴࡶࠪὍ"))
    @classmethod
    def bstack111111l11ll_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack1lll11l_opy_ (u"࠭ࡩࡥࠩ὎"): id(step),
                bstack1lll11l_opy_ (u"ࠧࡵࡧࡻࡸࠬ὏"): step.name,
                bstack1lll11l_opy_ (u"ࠨ࡭ࡨࡽࡼࡵࡲࡥࠩὐ"): step.keyword,
            })
        return bstack11llllll_opy_(
            **kwargs,
            meta={
                bstack1lll11l_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࠪὑ"): {
                    bstack1lll11l_opy_ (u"ࠪࡲࡦࡳࡥࠨὒ"): feature.name,
                    bstack1lll11l_opy_ (u"ࠫࡵࡧࡴࡩࠩὓ"): feature.filename,
                    bstack1lll11l_opy_ (u"ࠬࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪὔ"): feature.description
                },
                bstack1lll11l_opy_ (u"࠭ࡳࡤࡧࡱࡥࡷ࡯࡯ࠨὕ"): {
                    bstack1lll11l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬὖ"): scenario.name
                },
                bstack1lll11l_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧὗ"): steps,
                bstack1lll11l_opy_ (u"ࠩࡨࡼࡦࡳࡰ࡭ࡧࡶࠫ὘"): bstack11l111l11l1_opy_(test)
            }
        )
    def bstack111111ll11l_opy_(self):
        return {
            bstack1lll11l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩὙ"): self.hooks
        }
    def bstack1111111ll11_opy_(self):
        if self.bstack1l1l11l1_opy_:
            return {
                bstack1lll11l_opy_ (u"ࠫ࡮ࡴࡴࡦࡩࡵࡥࡹ࡯࡯࡯ࡵࠪ὚"): self.bstack1l1l11l1_opy_
            }
        return {}
    def bstack111111ll111_opy_(self):
        return {
            **super().bstack111111ll111_opy_(),
            **self.bstack111111ll11l_opy_()
        }
    def bstack111111l1lll_opy_(self):
        return {
            **super().bstack111111l1lll_opy_(),
            **self.bstack1111111ll11_opy_()
        }
    def event_key(self):
        return bstack1lll11l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧὛ")
class bstack1l111111_opy_(bstack11lllll1_opy_):
    def __init__(self, hook_type, *args,bstack1l1l11l1_opy_={}, **kwargs):
        self.hook_type = hook_type
        self.bstack1l1111l1l1l_opy_ = None
        self.bstack1l1l11l1_opy_ = bstack1l1l11l1_opy_
        super().__init__(*args, **kwargs, bstack11111l11ll_opy_=bstack1lll11l_opy_ (u"࠭ࡨࡰࡱ࡮ࠫ὜"))
    def bstack1l1l1l11_opy_(self):
        return self.hook_type
    def bstack1111111llll_opy_(self):
        return {
            bstack1lll11l_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧࠪὝ"): self.hook_type
        }
    def bstack111111ll111_opy_(self):
        return {
            **super().bstack111111ll111_opy_(),
            **self.bstack1111111llll_opy_()
        }
    def bstack111111l1lll_opy_(self):
        return {
            **super().bstack111111l1lll_opy_(),
            bstack1lll11l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢ࡭ࡩ࠭὞"): self.bstack1l1111l1l1l_opy_,
            **self.bstack1111111llll_opy_()
        }
    def event_key(self):
        return bstack1lll11l_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࠫὟ")
    def bstack11l111ll_opy_(self, bstack1l1111l1l1l_opy_):
        self.bstack1l1111l1l1l_opy_ = bstack1l1111l1l1l_opy_