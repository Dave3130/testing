# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
import os
from uuid import uuid4
from bstack_utils.helper import bstack1lll1111_opy_, bstack111l11l11ll_opy_
from bstack_utils.bstack1l11l111l1_opy_ import bstack11l111lll11_opy_
class bstack1l111l11_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, started_at=None, framework=None, tags=[], scope=[], bstack111111lll1l_opy_=None, bstack11111l1l1ll_opy_=True, bstack1ll1l1111ll_opy_=None, bstack1l11ll11ll_opy_=None, result=None, duration=None, bstack1ll11lll_opy_=None, meta={}):
        self.bstack1ll11lll_opy_ = bstack1ll11lll_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack11111l1l1ll_opy_:
            self.uuid = uuid4().__str__()
        self.started_at = started_at
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack111111lll1l_opy_ = bstack111111lll1l_opy_
        self.bstack1ll1l1111ll_opy_ = bstack1ll1l1111ll_opy_
        self.bstack1l11ll11ll_opy_ = bstack1l11ll11ll_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
        self.hooks = []
    def bstack11lllll1_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack11ll1l1l_opy_(self, meta):
        self.meta = meta
    def bstack11l1l1ll_opy_(self, hooks):
        self.hooks = hooks
    def bstack111111ll1ll_opy_(self):
        bstack11111l111l1_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack1ll11_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫủ"): bstack11111l111l1_opy_,
            bstack1ll11_opy_ (u"ࠩ࡯ࡳࡨࡧࡴࡪࡱࡱࠫỨ"): bstack11111l111l1_opy_,
            bstack1ll11_opy_ (u"ࠪࡺࡨࡥࡦࡪ࡮ࡨࡴࡦࡺࡨࠨứ"): bstack11111l111l1_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack1ll11_opy_ (u"࡚ࠦࡴࡥࡹࡲࡨࡧࡹ࡫ࡤࠡࡣࡵ࡫ࡺࡳࡥ࡯ࡶ࠽ࠤࠧỪ") + key)
            setattr(self, key, val)
    def bstack111111llll1_opy_(self):
        return {
            bstack1ll11_opy_ (u"ࠬࡴࡡ࡮ࡧࠪừ"): self.name,
            bstack1ll11_opy_ (u"࠭ࡢࡰࡦࡼࠫỬ"): {
                bstack1ll11_opy_ (u"ࠧ࡭ࡣࡱ࡫ࠬử"): bstack1ll11_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨỮ"),
                bstack1ll11_opy_ (u"ࠩࡦࡳࡩ࡫ࠧữ"): self.code
            },
            bstack1ll11_opy_ (u"ࠪࡷࡨࡵࡰࡦࡵࠪỰ"): self.scope,
            bstack1ll11_opy_ (u"ࠫࡹࡧࡧࡴࠩự"): self.tags,
            bstack1ll11_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨỲ"): self.framework,
            bstack1ll11_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪỳ"): self.started_at
        }
    def bstack11111l1l1l1_opy_(self):
        return {
         bstack1ll11_opy_ (u"ࠧ࡮ࡧࡷࡥࠬỴ"): self.meta
        }
    def bstack11111l111ll_opy_(self):
        return {
            bstack1ll11_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡓࡧࡵࡹࡳࡖࡡࡳࡣࡰࠫỵ"): {
                bstack1ll11_opy_ (u"ࠩࡵࡩࡷࡻ࡮ࡠࡰࡤࡱࡪ࠭Ỷ"): self.bstack111111lll1l_opy_
            }
        }
    def bstack11111l11ll1_opy_(self, bstack11111l11lll_opy_, details):
        step = next(filter(lambda st: st[bstack1ll11_opy_ (u"ࠪ࡭ࡩ࠭ỷ")] == bstack11111l11lll_opy_, self.meta[bstack1ll11_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪỸ")]), None)
        step.update(details)
    def bstack11ll1ll1_opy_(self, bstack11111l11lll_opy_):
        step = next(filter(lambda st: st[bstack1ll11_opy_ (u"ࠬ࡯ࡤࠨỹ")] == bstack11111l11lll_opy_, self.meta[bstack1ll11_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬỺ")]), None)
        step.update({
            bstack1ll11_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫỻ"): bstack1lll1111_opy_()
        })
    def bstack1ll11l1l_opy_(self, bstack11111l11lll_opy_, result, duration=None):
        bstack1ll1l1111ll_opy_ = bstack1lll1111_opy_()
        if bstack11111l11lll_opy_ is not None and self.meta.get(bstack1ll11_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧỼ")):
            step = next(filter(lambda st: st[bstack1ll11_opy_ (u"ࠩ࡬ࡨࠬỽ")] == bstack11111l11lll_opy_, self.meta[bstack1ll11_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩỾ")]), None)
            step.update({
                bstack1ll11_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩỿ"): bstack1ll1l1111ll_opy_,
                bstack1ll11_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧἀ"): duration if duration else bstack111l11l11ll_opy_(step[bstack1ll11_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪἁ")], bstack1ll1l1111ll_opy_),
                bstack1ll11_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧἂ"): result.result,
                bstack1ll11_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩἃ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack111111lllll_opy_):
        if self.meta.get(bstack1ll11_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨἄ")):
            self.meta[bstack1ll11_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩἅ")].append(bstack111111lllll_opy_)
        else:
            self.meta[bstack1ll11_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪἆ")] = [ bstack111111lllll_opy_ ]
    def bstack11111l1111l_opy_(self):
        return {
            bstack1ll11_opy_ (u"ࠬࡻࡵࡪࡦࠪἇ"): self.bstack11lllll1_opy_(),
            **self.bstack111111llll1_opy_(),
            **self.bstack111111ll1ll_opy_(),
            **self.bstack11111l1l1l1_opy_()
        }
    def bstack11111l11111_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack1ll11_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫἈ"): self.bstack1ll1l1111ll_opy_,
            bstack1ll11_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡤࡳࡳࠨἉ"): self.duration,
            bstack1ll11_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨἊ"): self.result.result
        }
        if data[bstack1ll11_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩἋ")] == bstack1ll11_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪἌ"):
            data[bstack1ll11_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠪἍ")] = self.result.bstack11111l111l_opy_()
            data[bstack1ll11_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭Ἆ")] = [{bstack1ll11_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩἏ"): self.result.bstack111l1l111ll_opy_()}]
        return data
    def bstack11111l1l11l_opy_(self):
        return {
            bstack1ll11_opy_ (u"ࠧࡶࡷ࡬ࡨࠬἐ"): self.bstack11lllll1_opy_(),
            **self.bstack111111llll1_opy_(),
            **self.bstack111111ll1ll_opy_(),
            **self.bstack11111l11111_opy_(),
            **self.bstack11111l1l1l1_opy_()
        }
    def bstack1l11l1l1_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack1ll11_opy_ (u"ࠨࡕࡷࡥࡷࡺࡥࡥࠩἑ") in event:
            return self.bstack11111l1111l_opy_()
        elif bstack1ll11_opy_ (u"ࠩࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫἒ") in event:
            return self.bstack11111l1l11l_opy_()
    def event_key(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1ll1l1111ll_opy_ = time if time else bstack1lll1111_opy_()
        self.duration = duration if duration else bstack111l11l11ll_opy_(self.started_at, self.bstack1ll1l1111ll_opy_)
        if result:
            self.result = result
class bstack1l1l1l1l_opy_(bstack1l111l11_opy_):
    def __init__(self, hooks=[], bstack11lll111_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack11lll111_opy_ = bstack11lll111_opy_
        super().__init__(*args, **kwargs, bstack1l11ll11ll_opy_=bstack1ll11_opy_ (u"ࠪࡸࡪࡹࡴࠨἓ"))
    @classmethod
    def bstack11111l11l11_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack1ll11_opy_ (u"ࠫ࡮ࡪࠧἔ"): id(step),
                bstack1ll11_opy_ (u"ࠬࡺࡥࡹࡶࠪἕ"): step.name,
                bstack1ll11_opy_ (u"࠭࡫ࡦࡻࡺࡳࡷࡪࠧ἖"): step.keyword,
            })
        return bstack1l1l1l1l_opy_(
            **kwargs,
            meta={
                bstack1ll11_opy_ (u"ࠧࡧࡧࡤࡸࡺࡸࡥࠨ἗"): {
                    bstack1ll11_opy_ (u"ࠨࡰࡤࡱࡪ࠭Ἐ"): feature.name,
                    bstack1ll11_opy_ (u"ࠩࡳࡥࡹ࡮ࠧἙ"): feature.filename,
                    bstack1ll11_opy_ (u"ࠪࡨࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠨἚ"): feature.description
                },
                bstack1ll11_opy_ (u"ࠫࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭Ἓ"): {
                    bstack1ll11_opy_ (u"ࠬࡴࡡ࡮ࡧࠪἜ"): scenario.name
                },
                bstack1ll11_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬἝ"): steps,
                bstack1ll11_opy_ (u"ࠧࡦࡺࡤࡱࡵࡲࡥࡴࠩ἞"): bstack11l111lll11_opy_(test)
            }
        )
    def bstack11111l1l111_opy_(self):
        return {
            bstack1ll11_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧ἟"): self.hooks
        }
    def bstack111111lll11_opy_(self):
        if self.bstack11lll111_opy_:
            return {
                bstack1ll11_opy_ (u"ࠩ࡬ࡲࡹ࡫ࡧࡳࡣࡷ࡭ࡴࡴࡳࠨἠ"): self.bstack11lll111_opy_
            }
        return {}
    def bstack11111l1l11l_opy_(self):
        return {
            **super().bstack11111l1l11l_opy_(),
            **self.bstack11111l1l111_opy_()
        }
    def bstack11111l1111l_opy_(self):
        return {
            **super().bstack11111l1111l_opy_(),
            **self.bstack111111lll11_opy_()
        }
    def event_key(self):
        return bstack1ll11_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࠬἡ")
class bstack1l111l1l_opy_(bstack1l111l11_opy_):
    def __init__(self, hook_type, *args,bstack11lll111_opy_={}, **kwargs):
        self.hook_type = hook_type
        self.bstack1l111l1lll1_opy_ = None
        self.bstack11lll111_opy_ = bstack11lll111_opy_
        super().__init__(*args, **kwargs, bstack1l11ll11ll_opy_=bstack1ll11_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩἢ"))
    def bstack1lll1l11_opy_(self):
        return self.hook_type
    def bstack11111l11l1l_opy_(self):
        return {
            bstack1ll11_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨἣ"): self.hook_type
        }
    def bstack11111l1l11l_opy_(self):
        return {
            **super().bstack11111l1l11l_opy_(),
            **self.bstack11111l11l1l_opy_()
        }
    def bstack11111l1111l_opy_(self):
        return {
            **super().bstack11111l1111l_opy_(),
            bstack1ll11_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠ࡫ࡧࠫἤ"): self.bstack1l111l1lll1_opy_,
            **self.bstack11111l11l1l_opy_()
        }
    def event_key(self):
        return bstack1ll11_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࠩἥ")
    def bstack11ll1l11_opy_(self, bstack1l111l1lll1_opy_):
        self.bstack1l111l1lll1_opy_ = bstack1l111l1lll1_opy_