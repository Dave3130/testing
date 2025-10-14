# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
import os
from uuid import uuid4
from bstack_utils.helper import bstack1ll1ll11_opy_, bstack1111l1ll11l_opy_
from bstack_utils.bstack1ll111lll_opy_ import bstack11l11l11ll1_opy_
class bstack1lll1l11_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, started_at=None, framework=None, tags=[], scope=[], bstack111111lll1l_opy_=None, bstack11111l111l1_opy_=True, bstack1ll1l1lllll_opy_=None, bstack11111111l_opy_=None, result=None, duration=None, bstack11llll1l_opy_=None, meta={}):
        self.bstack11llll1l_opy_ = bstack11llll1l_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack11111l111l1_opy_:
            self.uuid = uuid4().__str__()
        self.started_at = started_at
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack111111lll1l_opy_ = bstack111111lll1l_opy_
        self.bstack1ll1l1lllll_opy_ = bstack1ll1l1lllll_opy_
        self.bstack11111111l_opy_ = bstack11111111l_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
        self.hooks = []
    def bstack1lll11l1_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack11l1l1ll_opy_(self, meta):
        self.meta = meta
    def bstack11l1ll11_opy_(self, hooks):
        self.hooks = hooks
    def bstack11111l1l11l_opy_(self):
        bstack11111l11l1l_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack11l1l11_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫỠ"): bstack11111l11l1l_opy_,
            bstack11l1l11_opy_ (u"ࠩ࡯ࡳࡨࡧࡴࡪࡱࡱࠫỡ"): bstack11111l11l1l_opy_,
            bstack11l1l11_opy_ (u"ࠪࡺࡨࡥࡦࡪ࡮ࡨࡴࡦࡺࡨࠨỢ"): bstack11111l11l1l_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack11l1l11_opy_ (u"࡚ࠦࡴࡥࡹࡲࡨࡧࡹ࡫ࡤࠡࡣࡵ࡫ࡺࡳࡥ࡯ࡶ࠽ࠤࠧợ") + key)
            setattr(self, key, val)
    def bstack11111l111ll_opy_(self):
        return {
            bstack11l1l11_opy_ (u"ࠬࡴࡡ࡮ࡧࠪỤ"): self.name,
            bstack11l1l11_opy_ (u"࠭ࡢࡰࡦࡼࠫụ"): {
                bstack11l1l11_opy_ (u"ࠧ࡭ࡣࡱ࡫ࠬỦ"): bstack11l1l11_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨủ"),
                bstack11l1l11_opy_ (u"ࠩࡦࡳࡩ࡫ࠧỨ"): self.code
            },
            bstack11l1l11_opy_ (u"ࠪࡷࡨࡵࡰࡦࡵࠪứ"): self.scope,
            bstack11l1l11_opy_ (u"ࠫࡹࡧࡧࡴࠩỪ"): self.tags,
            bstack11l1l11_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨừ"): self.framework,
            bstack11l1l11_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪỬ"): self.started_at
        }
    def bstack111111lllll_opy_(self):
        return {
         bstack11l1l11_opy_ (u"ࠧ࡮ࡧࡷࡥࠬử"): self.meta
        }
    def bstack111111llll1_opy_(self):
        return {
            bstack11l1l11_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡓࡧࡵࡹࡳࡖࡡࡳࡣࡰࠫỮ"): {
                bstack11l1l11_opy_ (u"ࠩࡵࡩࡷࡻ࡮ࡠࡰࡤࡱࡪ࠭ữ"): self.bstack111111lll1l_opy_
            }
        }
    def bstack11111l1l111_opy_(self, bstack111111ll1ll_opy_, details):
        step = next(filter(lambda st: st[bstack11l1l11_opy_ (u"ࠪ࡭ࡩ࠭Ự")] == bstack111111ll1ll_opy_, self.meta[bstack11l1l11_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪự")]), None)
        step.update(details)
    def bstack11ll11l1_opy_(self, bstack111111ll1ll_opy_):
        step = next(filter(lambda st: st[bstack11l1l11_opy_ (u"ࠬ࡯ࡤࠨỲ")] == bstack111111ll1ll_opy_, self.meta[bstack11l1l11_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬỳ")]), None)
        step.update({
            bstack11l1l11_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫỴ"): bstack1ll1ll11_opy_()
        })
    def bstack1lll11ll_opy_(self, bstack111111ll1ll_opy_, result, duration=None):
        bstack1ll1l1lllll_opy_ = bstack1ll1ll11_opy_()
        if bstack111111ll1ll_opy_ is not None and self.meta.get(bstack11l1l11_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧỵ")):
            step = next(filter(lambda st: st[bstack11l1l11_opy_ (u"ࠩ࡬ࡨࠬỶ")] == bstack111111ll1ll_opy_, self.meta[bstack11l1l11_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩỷ")]), None)
            step.update({
                bstack11l1l11_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩỸ"): bstack1ll1l1lllll_opy_,
                bstack11l1l11_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧỹ"): duration if duration else bstack1111l1ll11l_opy_(step[bstack11l1l11_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪỺ")], bstack1ll1l1lllll_opy_),
                bstack11l1l11_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧỻ"): result.result,
                bstack11l1l11_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩỼ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack11111l11lll_opy_):
        if self.meta.get(bstack11l1l11_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨỽ")):
            self.meta[bstack11l1l11_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩỾ")].append(bstack11111l11lll_opy_)
        else:
            self.meta[bstack11l1l11_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪỿ")] = [ bstack11111l11lll_opy_ ]
    def bstack11111l1111l_opy_(self):
        return {
            bstack11l1l11_opy_ (u"ࠬࡻࡵࡪࡦࠪἀ"): self.bstack1lll11l1_opy_(),
            **self.bstack11111l111ll_opy_(),
            **self.bstack11111l1l11l_opy_(),
            **self.bstack111111lllll_opy_()
        }
    def bstack111111ll1l1_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack11l1l11_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫἁ"): self.bstack1ll1l1lllll_opy_,
            bstack11l1l11_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡤࡳࡳࠨἂ"): self.duration,
            bstack11l1l11_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨἃ"): self.result.result
        }
        if data[bstack11l1l11_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩἄ")] == bstack11l1l11_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪἅ"):
            data[bstack11l1l11_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠪἆ")] = self.result.bstack11111l111l_opy_()
            data[bstack11l1l11_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭ἇ")] = [{bstack11l1l11_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩἈ"): self.result.bstack111l1llllll_opy_()}]
        return data
    def bstack11111l11ll1_opy_(self):
        return {
            bstack11l1l11_opy_ (u"ࠧࡶࡷ࡬ࡨࠬἉ"): self.bstack1lll11l1_opy_(),
            **self.bstack11111l111ll_opy_(),
            **self.bstack11111l1l11l_opy_(),
            **self.bstack111111ll1l1_opy_(),
            **self.bstack111111lllll_opy_()
        }
    def bstack11lll1ll_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack11l1l11_opy_ (u"ࠨࡕࡷࡥࡷࡺࡥࡥࠩἊ") in event:
            return self.bstack11111l1111l_opy_()
        elif bstack11l1l11_opy_ (u"ࠩࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫἋ") in event:
            return self.bstack11111l11ll1_opy_()
    def event_key(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1ll1l1lllll_opy_ = time if time else bstack1ll1ll11_opy_()
        self.duration = duration if duration else bstack1111l1ll11l_opy_(self.started_at, self.bstack1ll1l1lllll_opy_)
        if result:
            self.result = result
class bstack11lllll1_opy_(bstack1lll1l11_opy_):
    def __init__(self, hooks=[], bstack1l111ll1_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack1l111ll1_opy_ = bstack1l111ll1_opy_
        super().__init__(*args, **kwargs, bstack11111111l_opy_=bstack11l1l11_opy_ (u"ࠪࡸࡪࡹࡴࠨἌ"))
    @classmethod
    def bstack11111l11111_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack11l1l11_opy_ (u"ࠫ࡮ࡪࠧἍ"): id(step),
                bstack11l1l11_opy_ (u"ࠬࡺࡥࡹࡶࠪἎ"): step.name,
                bstack11l1l11_opy_ (u"࠭࡫ࡦࡻࡺࡳࡷࡪࠧἏ"): step.keyword,
            })
        return bstack11lllll1_opy_(
            **kwargs,
            meta={
                bstack11l1l11_opy_ (u"ࠧࡧࡧࡤࡸࡺࡸࡥࠨἐ"): {
                    bstack11l1l11_opy_ (u"ࠨࡰࡤࡱࡪ࠭ἑ"): feature.name,
                    bstack11l1l11_opy_ (u"ࠩࡳࡥࡹ࡮ࠧἒ"): feature.filename,
                    bstack11l1l11_opy_ (u"ࠪࡨࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠨἓ"): feature.description
                },
                bstack11l1l11_opy_ (u"ࠫࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭ἔ"): {
                    bstack11l1l11_opy_ (u"ࠬࡴࡡ࡮ࡧࠪἕ"): scenario.name
                },
                bstack11l1l11_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬ἖"): steps,
                bstack11l1l11_opy_ (u"ࠧࡦࡺࡤࡱࡵࡲࡥࡴࠩ἗"): bstack11l11l11ll1_opy_(test)
            }
        )
    def bstack11111l11l11_opy_(self):
        return {
            bstack11l1l11_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧἘ"): self.hooks
        }
    def bstack111111lll11_opy_(self):
        if self.bstack1l111ll1_opy_:
            return {
                bstack11l1l11_opy_ (u"ࠩ࡬ࡲࡹ࡫ࡧࡳࡣࡷ࡭ࡴࡴࡳࠨἙ"): self.bstack1l111ll1_opy_
            }
        return {}
    def bstack11111l11ll1_opy_(self):
        return {
            **super().bstack11111l11ll1_opy_(),
            **self.bstack11111l11l11_opy_()
        }
    def bstack11111l1111l_opy_(self):
        return {
            **super().bstack11111l1111l_opy_(),
            **self.bstack111111lll11_opy_()
        }
    def event_key(self):
        return bstack11l1l11_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࠬἚ")
class bstack1l111l1l_opy_(bstack1lll1l11_opy_):
    def __init__(self, hook_type, *args,bstack1l111ll1_opy_={}, **kwargs):
        self.hook_type = hook_type
        self.bstack1l111ll1lll_opy_ = None
        self.bstack1l111ll1_opy_ = bstack1l111ll1_opy_
        super().__init__(*args, **kwargs, bstack11111111l_opy_=bstack11l1l11_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩἛ"))
    def bstack1ll11l1l_opy_(self):
        return self.hook_type
    def bstack11111l1l1l1_opy_(self):
        return {
            bstack11l1l11_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨἜ"): self.hook_type
        }
    def bstack11111l11ll1_opy_(self):
        return {
            **super().bstack11111l11ll1_opy_(),
            **self.bstack11111l1l1l1_opy_()
        }
    def bstack11111l1111l_opy_(self):
        return {
            **super().bstack11111l1111l_opy_(),
            bstack11l1l11_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠ࡫ࡧࠫἝ"): self.bstack1l111ll1lll_opy_,
            **self.bstack11111l1l1l1_opy_()
        }
    def event_key(self):
        return bstack11l1l11_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࠩ἞")
    def bstack11ll1ll1_opy_(self, bstack1l111ll1lll_opy_):
        self.bstack1l111ll1lll_opy_ = bstack1l111ll1lll_opy_