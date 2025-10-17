# coding: UTF-8
import sys
bstack111l11_opy_ = sys.version_info [0] == 2
bstack111ll1l_opy_ = 2048
bstack1_opy_ = 7
def bstack11111_opy_ (bstack1l111ll_opy_):
    global bstack111ll11_opy_
    bstack1lllll_opy_ = ord (bstack1l111ll_opy_ [-1])
    bstack1l1llll_opy_ = bstack1l111ll_opy_ [:-1]
    bstack11l11l_opy_ = bstack1lllll_opy_ % len (bstack1l1llll_opy_)
    bstack111l_opy_ = bstack1l1llll_opy_ [:bstack11l11l_opy_] + bstack1l1llll_opy_ [bstack11l11l_opy_:]
    if bstack111l11_opy_:
        bstack1l1l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1l1l1l_opy_ = str () .join ([chr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1l1l1l_opy_)
import os
from uuid import uuid4
from bstack_utils.helper import bstack1l11llll_opy_, bstack111l11l11l1_opy_
from bstack_utils.bstack1ll11lll1_opy_ import bstack11l11l1111l_opy_
class bstack1ll11ll1_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, started_at=None, framework=None, tags=[], scope=[], bstack11111l11lll_opy_=None, bstack111111lllll_opy_=True, bstack1ll1l1l111l_opy_=None, bstack1ll1l1l1l_opy_=None, result=None, duration=None, bstack1ll1l1l1_opy_=None, meta={}):
        self.bstack1ll1l1l1_opy_ = bstack1ll1l1l1_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack111111lllll_opy_:
            self.uuid = uuid4().__str__()
        self.started_at = started_at
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack11111l11lll_opy_ = bstack11111l11lll_opy_
        self.bstack1ll1l1l111l_opy_ = bstack1ll1l1l111l_opy_
        self.bstack1ll1l1l1l_opy_ = bstack1ll1l1l1l_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
        self.hooks = []
    def bstack1llll1l1_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack11ll1111_opy_(self, meta):
        self.meta = meta
    def bstack11ll11ll_opy_(self, hooks):
        self.hooks = hooks
    def bstack111111llll1_opy_(self):
        bstack11111l1l111_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack11111_opy_ (u"ࠧࡧ࡫࡯ࡩࡤࡴࡡ࡮ࡧࠪỘ"): bstack11111l1l111_opy_,
            bstack11111_opy_ (u"ࠨ࡮ࡲࡧࡦࡺࡩࡰࡰࠪộ"): bstack11111l1l111_opy_,
            bstack11111_opy_ (u"ࠩࡹࡧࡤ࡬ࡩ࡭ࡧࡳࡥࡹ࡮ࠧỚ"): bstack11111l1l111_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack11111_opy_ (u"࡙ࠥࡳ࡫ࡸࡱࡧࡦࡸࡪࡪࠠࡢࡴࡪࡹࡲ࡫࡮ࡵ࠼ࠣࠦớ") + key)
            setattr(self, key, val)
    def bstack11111l11ll1_opy_(self):
        return {
            bstack11111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩỜ"): self.name,
            bstack11111_opy_ (u"ࠬࡨ࡯ࡥࡻࠪờ"): {
                bstack11111_opy_ (u"࠭࡬ࡢࡰࡪࠫỞ"): bstack11111_opy_ (u"ࠧࡱࡻࡷ࡬ࡴࡴࠧở"),
                bstack11111_opy_ (u"ࠨࡥࡲࡨࡪ࠭Ỡ"): self.code
            },
            bstack11111_opy_ (u"ࠩࡶࡧࡴࡶࡥࡴࠩỡ"): self.scope,
            bstack11111_opy_ (u"ࠪࡸࡦ࡭ࡳࠨỢ"): self.tags,
            bstack11111_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧợ"): self.framework,
            bstack11111_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩỤ"): self.started_at
        }
    def bstack11111l11l1l_opy_(self):
        return {
         bstack11111_opy_ (u"࠭࡭ࡦࡶࡤࠫụ"): self.meta
        }
    def bstack111111ll1ll_opy_(self):
        return {
            bstack11111_opy_ (u"ࠧࡤࡷࡶࡸࡴࡳࡒࡦࡴࡸࡲࡕࡧࡲࡢ࡯ࠪỦ"): {
                bstack11111_opy_ (u"ࠨࡴࡨࡶࡺࡴ࡟࡯ࡣࡰࡩࠬủ"): self.bstack11111l11lll_opy_
            }
        }
    def bstack11111l111ll_opy_(self, bstack111111ll11l_opy_, details):
        step = next(filter(lambda st: st[bstack11111_opy_ (u"ࠩ࡬ࡨࠬỨ")] == bstack111111ll11l_opy_, self.meta[bstack11111_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩứ")]), None)
        step.update(details)
    def bstack11ll1lll_opy_(self, bstack111111ll11l_opy_):
        step = next(filter(lambda st: st[bstack11111_opy_ (u"ࠫ࡮ࡪࠧỪ")] == bstack111111ll11l_opy_, self.meta[bstack11111_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫừ")]), None)
        step.update({
            bstack11111_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪỬ"): bstack1l11llll_opy_()
        })
    def bstack1l1l1111_opy_(self, bstack111111ll11l_opy_, result, duration=None):
        bstack1ll1l1l111l_opy_ = bstack1l11llll_opy_()
        if bstack111111ll11l_opy_ is not None and self.meta.get(bstack11111_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ử")):
            step = next(filter(lambda st: st[bstack11111_opy_ (u"ࠨ࡫ࡧࠫỮ")] == bstack111111ll11l_opy_, self.meta[bstack11111_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨữ")]), None)
            step.update({
                bstack11111_opy_ (u"ࠪࡪ࡮ࡴࡩࡴࡪࡨࡨࡤࡧࡴࠨỰ"): bstack1ll1l1l111l_opy_,
                bstack11111_opy_ (u"ࠫࡩࡻࡲࡢࡶ࡬ࡳࡳ࠭ự"): duration if duration else bstack111l11l11l1_opy_(step[bstack11111_opy_ (u"ࠬࡹࡴࡢࡴࡷࡩࡩࡥࡡࡵࠩỲ")], bstack1ll1l1l111l_opy_),
                bstack11111_opy_ (u"࠭ࡲࡦࡵࡸࡰࡹ࠭ỳ"): result.result,
                bstack11111_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨỴ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack11111l11111_opy_):
        if self.meta.get(bstack11111_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧỵ")):
            self.meta[bstack11111_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨỶ")].append(bstack11111l11111_opy_)
        else:
            self.meta[bstack11111_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩỷ")] = [ bstack11111l11111_opy_ ]
    def bstack111111lll11_opy_(self):
        return {
            bstack11111_opy_ (u"ࠫࡺࡻࡩࡥࠩỸ"): self.bstack1llll1l1_opy_(),
            **self.bstack11111l11ll1_opy_(),
            **self.bstack111111llll1_opy_(),
            **self.bstack11111l11l1l_opy_()
        }
    def bstack11111l11l11_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack11111_opy_ (u"ࠬ࡬ࡩ࡯࡫ࡶ࡬ࡪࡪ࡟ࡢࡶࠪỹ"): self.bstack1ll1l1l111l_opy_,
            bstack11111_opy_ (u"࠭ࡤࡶࡴࡤࡸ࡮ࡵ࡮ࡠ࡫ࡱࡣࡲࡹࠧỺ"): self.duration,
            bstack11111_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧỻ"): self.result.result
        }
        if data[bstack11111_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨỼ")] == bstack11111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩỽ"):
            data[bstack11111_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࡣࡹࡿࡰࡦࠩỾ")] = self.result.bstack111111lll1_opy_()
            data[bstack11111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬỿ")] = [{bstack11111_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨἀ"): self.result.bstack111ll111111_opy_()}]
        return data
    def bstack111111ll1l1_opy_(self):
        return {
            bstack11111_opy_ (u"࠭ࡵࡶ࡫ࡧࠫἁ"): self.bstack1llll1l1_opy_(),
            **self.bstack11111l11ll1_opy_(),
            **self.bstack111111llll1_opy_(),
            **self.bstack11111l11l11_opy_(),
            **self.bstack11111l11l1l_opy_()
        }
    def bstack1l11111l_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack11111_opy_ (u"ࠧࡔࡶࡤࡶࡹ࡫ࡤࠨἂ") in event:
            return self.bstack111111lll11_opy_()
        elif bstack11111_opy_ (u"ࠨࡈ࡬ࡲ࡮ࡹࡨࡦࡦࠪἃ") in event:
            return self.bstack111111ll1l1_opy_()
    def event_key(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1ll1l1l111l_opy_ = time if time else bstack1l11llll_opy_()
        self.duration = duration if duration else bstack111l11l11l1_opy_(self.started_at, self.bstack1ll1l1l111l_opy_)
        if result:
            self.result = result
class bstack1ll1111l_opy_(bstack1ll11ll1_opy_):
    def __init__(self, hooks=[], bstack1lll11ll_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack1lll11ll_opy_ = bstack1lll11ll_opy_
        super().__init__(*args, **kwargs, bstack1ll1l1l1l_opy_=bstack11111_opy_ (u"ࠩࡷࡩࡸࡺࠧἄ"))
    @classmethod
    def bstack11111l1111l_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack11111_opy_ (u"ࠪ࡭ࡩ࠭ἅ"): id(step),
                bstack11111_opy_ (u"ࠫࡹ࡫ࡸࡵࠩἆ"): step.name,
                bstack11111_opy_ (u"ࠬࡱࡥࡺࡹࡲࡶࡩ࠭ἇ"): step.keyword,
            })
        return bstack1ll1111l_opy_(
            **kwargs,
            meta={
                bstack11111_opy_ (u"࠭ࡦࡦࡣࡷࡹࡷ࡫ࠧἈ"): {
                    bstack11111_opy_ (u"ࠧ࡯ࡣࡰࡩࠬἉ"): feature.name,
                    bstack11111_opy_ (u"ࠨࡲࡤࡸ࡭࠭Ἂ"): feature.filename,
                    bstack11111_opy_ (u"ࠩࡧࡩࡸࡩࡲࡪࡲࡷ࡭ࡴࡴࠧἋ"): feature.description
                },
                bstack11111_opy_ (u"ࠪࡷࡨ࡫࡮ࡢࡴ࡬ࡳࠬἌ"): {
                    bstack11111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩἍ"): scenario.name
                },
                bstack11111_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫἎ"): steps,
                bstack11111_opy_ (u"࠭ࡥࡹࡣࡰࡴࡱ࡫ࡳࠨἏ"): bstack11l11l1111l_opy_(test)
            }
        )
    def bstack111111lll1l_opy_(self):
        return {
            bstack11111_opy_ (u"ࠧࡩࡱࡲ࡯ࡸ࠭ἐ"): self.hooks
        }
    def bstack111111ll111_opy_(self):
        if self.bstack1lll11ll_opy_:
            return {
                bstack11111_opy_ (u"ࠨ࡫ࡱࡸࡪ࡭ࡲࡢࡶ࡬ࡳࡳࡹࠧἑ"): self.bstack1lll11ll_opy_
            }
        return {}
    def bstack111111ll1l1_opy_(self):
        return {
            **super().bstack111111ll1l1_opy_(),
            **self.bstack111111lll1l_opy_()
        }
    def bstack111111lll11_opy_(self):
        return {
            **super().bstack111111lll11_opy_(),
            **self.bstack111111ll111_opy_()
        }
    def event_key(self):
        return bstack11111_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࠫἒ")
class bstack1l11l1ll_opy_(bstack1ll11ll1_opy_):
    def __init__(self, hook_type, *args,bstack1lll11ll_opy_={}, **kwargs):
        self.hook_type = hook_type
        self.bstack1l1111ll11l_opy_ = None
        self.bstack1lll11ll_opy_ = bstack1lll11ll_opy_
        super().__init__(*args, **kwargs, bstack1ll1l1l1l_opy_=bstack11111_opy_ (u"ࠪ࡬ࡴࡵ࡫ࠨἓ"))
    def bstack1l1ll1ll_opy_(self):
        return self.hook_type
    def bstack11111l111l1_opy_(self):
        return {
            bstack11111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡡࡷࡽࡵ࡫ࠧἔ"): self.hook_type
        }
    def bstack111111ll1l1_opy_(self):
        return {
            **super().bstack111111ll1l1_opy_(),
            **self.bstack11111l111l1_opy_()
        }
    def bstack111111lll11_opy_(self):
        return {
            **super().bstack111111lll11_opy_(),
            bstack11111_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴ࡟ࡪࡦࠪἕ"): self.bstack1l1111ll11l_opy_,
            **self.bstack11111l111l1_opy_()
        }
    def event_key(self):
        return bstack11111_opy_ (u"࠭ࡨࡰࡱ࡮ࡣࡷࡻ࡮ࠨ἖")
    def bstack11ll1l11_opy_(self, bstack1l1111ll11l_opy_):
        self.bstack1l1111ll11l_opy_ = bstack1l1111ll11l_opy_