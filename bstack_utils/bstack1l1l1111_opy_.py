# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11111l_opy_ = 7
def bstack1ll1ll1_opy_ (bstack11lll1l_opy_):
    global bstack1ll11l1_opy_
    bstack1l1ll_opy_ = ord (bstack11lll1l_opy_ [-1])
    bstack1ll1l1l_opy_ = bstack11lll1l_opy_ [:-1]
    bstack1l1l1ll_opy_ = bstack1l1ll_opy_ % len (bstack1ll1l1l_opy_)
    bstack11ll1ll_opy_ = bstack1ll1l1l_opy_ [:bstack1l1l1ll_opy_] + bstack1ll1l1l_opy_ [bstack1l1l1ll_opy_:]
    if bstack111ll1_opy_:
        bstack111ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    else:
        bstack111ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    return eval (bstack111ll_opy_)
import os
from uuid import uuid4
from bstack_utils.helper import bstack1l11l1ll_opy_, bstack1111l1l1ll1_opy_
from bstack_utils.bstack1l1lll11ll_opy_ import bstack11l111lll11_opy_
class bstack1lll1lll_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, started_at=None, framework=None, tags=[], scope=[], bstack111111ll1ll_opy_=None, bstack11111l11111_opy_=True, bstack1ll111llll1_opy_=None, bstack1lll111111_opy_=None, result=None, duration=None, bstack1l1111l1_opy_=None, meta={}):
        self.bstack1l1111l1_opy_ = bstack1l1111l1_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack11111l11111_opy_:
            self.uuid = uuid4().__str__()
        self.started_at = started_at
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack111111ll1ll_opy_ = bstack111111ll1ll_opy_
        self.bstack1ll111llll1_opy_ = bstack1ll111llll1_opy_
        self.bstack1lll111111_opy_ = bstack1lll111111_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
        self.hooks = []
    def bstack1l111ll1_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack11l1l1l1_opy_(self, meta):
        self.meta = meta
    def bstack11l1ll1l_opy_(self, hooks):
        self.hooks = hooks
    def bstack11111l11l11_opy_(self):
        bstack11111l11l1l_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack1ll1ll1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧỪ"): bstack11111l11l1l_opy_,
            bstack1ll1ll1_opy_ (u"ࠬࡲ࡯ࡤࡣࡷ࡭ࡴࡴࠧừ"): bstack11111l11l1l_opy_,
            bstack1ll1ll1_opy_ (u"࠭ࡶࡤࡡࡩ࡭ࡱ࡫ࡰࡢࡶ࡫ࠫỬ"): bstack11111l11l1l_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack1ll1ll1_opy_ (u"ࠢࡖࡰࡨࡼࡵ࡫ࡣࡵࡧࡧࠤࡦࡸࡧࡶ࡯ࡨࡲࡹࡀࠠࠣử") + key)
            setattr(self, key, val)
    def bstack11111l11lll_opy_(self):
        return {
            bstack1ll1ll1_opy_ (u"ࠨࡰࡤࡱࡪ࠭Ữ"): self.name,
            bstack1ll1ll1_opy_ (u"ࠩࡥࡳࡩࡿࠧữ"): {
                bstack1ll1ll1_opy_ (u"ࠪࡰࡦࡴࡧࠨỰ"): bstack1ll1ll1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫự"),
                bstack1ll1ll1_opy_ (u"ࠬࡩ࡯ࡥࡧࠪỲ"): self.code
            },
            bstack1ll1ll1_opy_ (u"࠭ࡳࡤࡱࡳࡩࡸ࠭ỳ"): self.scope,
            bstack1ll1ll1_opy_ (u"ࠧࡵࡣࡪࡷࠬỴ"): self.tags,
            bstack1ll1ll1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫỵ"): self.framework,
            bstack1ll1ll1_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭Ỷ"): self.started_at
        }
    def bstack111111llll1_opy_(self):
        return {
         bstack1ll1ll1_opy_ (u"ࠪࡱࡪࡺࡡࠨỷ"): self.meta
        }
    def bstack11111l11ll1_opy_(self):
        return {
            bstack1ll1ll1_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡖࡪࡸࡵ࡯ࡒࡤࡶࡦࡳࠧỸ"): {
                bstack1ll1ll1_opy_ (u"ࠬࡸࡥࡳࡷࡱࡣࡳࡧ࡭ࡦࠩỹ"): self.bstack111111ll1ll_opy_
            }
        }
    def bstack11111l111l1_opy_(self, bstack111111lll11_opy_, details):
        step = next(filter(lambda st: st[bstack1ll1ll1_opy_ (u"࠭ࡩࡥࠩỺ")] == bstack111111lll11_opy_, self.meta[bstack1ll1ll1_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ỻ")]), None)
        step.update(details)
    def bstack11l1l1ll_opy_(self, bstack111111lll11_opy_):
        step = next(filter(lambda st: st[bstack1ll1ll1_opy_ (u"ࠨ࡫ࡧࠫỼ")] == bstack111111lll11_opy_, self.meta[bstack1ll1ll1_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨỽ")]), None)
        step.update({
            bstack1ll1ll1_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧỾ"): bstack1l11l1ll_opy_()
        })
    def bstack1l11l11l_opy_(self, bstack111111lll11_opy_, result, duration=None):
        bstack1ll111llll1_opy_ = bstack1l11l1ll_opy_()
        if bstack111111lll11_opy_ is not None and self.meta.get(bstack1ll1ll1_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪỿ")):
            step = next(filter(lambda st: st[bstack1ll1ll1_opy_ (u"ࠬ࡯ࡤࠨἀ")] == bstack111111lll11_opy_, self.meta[bstack1ll1ll1_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬἁ")]), None)
            step.update({
                bstack1ll1ll1_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬἂ"): bstack1ll111llll1_opy_,
                bstack1ll1ll1_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࠪἃ"): duration if duration else bstack1111l1l1ll1_opy_(step[bstack1ll1ll1_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ἄ")], bstack1ll111llll1_opy_),
                bstack1ll1ll1_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪἅ"): result.result,
                bstack1ll1ll1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬἆ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack11111l1l1ll_opy_):
        if self.meta.get(bstack1ll1ll1_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫἇ")):
            self.meta[bstack1ll1ll1_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬἈ")].append(bstack11111l1l1ll_opy_)
        else:
            self.meta[bstack1ll1ll1_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭Ἁ")] = [ bstack11111l1l1ll_opy_ ]
    def bstack111111lllll_opy_(self):
        return {
            bstack1ll1ll1_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭Ἂ"): self.bstack1l111ll1_opy_(),
            **self.bstack11111l11lll_opy_(),
            **self.bstack11111l11l11_opy_(),
            **self.bstack111111llll1_opy_()
        }
    def bstack111111lll1l_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack1ll1ll1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧἋ"): self.bstack1ll111llll1_opy_,
            bstack1ll1ll1_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࡤ࡯࡮ࡠ࡯ࡶࠫἌ"): self.duration,
            bstack1ll1ll1_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫἍ"): self.result.result
        }
        if data[bstack1ll1ll1_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬἎ")] == bstack1ll1ll1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭Ἇ"):
            data[bstack1ll1ll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࡠࡶࡼࡴࡪ࠭ἐ")] = self.result.bstack11111l11l1_opy_()
            data[bstack1ll1ll1_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩἑ")] = [{bstack1ll1ll1_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬἒ"): self.result.bstack111l11l1111_opy_()}]
        return data
    def bstack11111l1l111_opy_(self):
        return {
            bstack1ll1ll1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨἓ"): self.bstack1l111ll1_opy_(),
            **self.bstack11111l11lll_opy_(),
            **self.bstack11111l11l11_opy_(),
            **self.bstack111111lll1l_opy_(),
            **self.bstack111111llll1_opy_()
        }
    def bstack11lll1l1_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack1ll1ll1_opy_ (u"ࠫࡘࡺࡡࡳࡶࡨࡨࠬἔ") in event:
            return self.bstack111111lllll_opy_()
        elif bstack1ll1ll1_opy_ (u"ࠬࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧἕ") in event:
            return self.bstack11111l1l111_opy_()
    def event_key(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1ll111llll1_opy_ = time if time else bstack1l11l1ll_opy_()
        self.duration = duration if duration else bstack1111l1l1ll1_opy_(self.started_at, self.bstack1ll111llll1_opy_)
        if result:
            self.result = result
class bstack1ll1lll1_opy_(bstack1lll1lll_opy_):
    def __init__(self, hooks=[], bstack1l111l1l_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack1l111l1l_opy_ = bstack1l111l1l_opy_
        super().__init__(*args, **kwargs, bstack1lll111111_opy_=bstack1ll1ll1_opy_ (u"࠭ࡴࡦࡵࡷࠫ἖"))
    @classmethod
    def bstack11111l111ll_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack1ll1ll1_opy_ (u"ࠧࡪࡦࠪ἗"): id(step),
                bstack1ll1ll1_opy_ (u"ࠨࡶࡨࡼࡹ࠭Ἐ"): step.name,
                bstack1ll1ll1_opy_ (u"ࠩ࡮ࡩࡾࡽ࡯ࡳࡦࠪἙ"): step.keyword,
            })
        return bstack1ll1lll1_opy_(
            **kwargs,
            meta={
                bstack1ll1ll1_opy_ (u"ࠪࡪࡪࡧࡴࡶࡴࡨࠫἚ"): {
                    bstack1ll1ll1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩἛ"): feature.name,
                    bstack1ll1ll1_opy_ (u"ࠬࡶࡡࡵࡪࠪἜ"): feature.filename,
                    bstack1ll1ll1_opy_ (u"࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫἝ"): feature.description
                },
                bstack1ll1ll1_opy_ (u"ࠧࡴࡥࡨࡲࡦࡸࡩࡰࠩ἞"): {
                    bstack1ll1ll1_opy_ (u"ࠨࡰࡤࡱࡪ࠭἟"): scenario.name
                },
                bstack1ll1ll1_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨἠ"): steps,
                bstack1ll1ll1_opy_ (u"ࠪࡩࡽࡧ࡭ࡱ࡮ࡨࡷࠬἡ"): bstack11l111lll11_opy_(test)
            }
        )
    def bstack11111l1l11l_opy_(self):
        return {
            bstack1ll1ll1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪἢ"): self.hooks
        }
    def bstack11111l1l1l1_opy_(self):
        if self.bstack1l111l1l_opy_:
            return {
                bstack1ll1ll1_opy_ (u"ࠬ࡯࡮ࡵࡧࡪࡶࡦࡺࡩࡰࡰࡶࠫἣ"): self.bstack1l111l1l_opy_
            }
        return {}
    def bstack11111l1l111_opy_(self):
        return {
            **super().bstack11111l1l111_opy_(),
            **self.bstack11111l1l11l_opy_()
        }
    def bstack111111lllll_opy_(self):
        return {
            **super().bstack111111lllll_opy_(),
            **self.bstack11111l1l1l1_opy_()
        }
    def event_key(self):
        return bstack1ll1ll1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࠨἤ")
class bstack1ll11ll1_opy_(bstack1lll1lll_opy_):
    def __init__(self, hook_type, *args,bstack1l111l1l_opy_={}, **kwargs):
        self.hook_type = hook_type
        self.bstack1l111llllll_opy_ = None
        self.bstack1l111l1l_opy_ = bstack1l111l1l_opy_
        super().__init__(*args, **kwargs, bstack1lll111111_opy_=bstack1ll1ll1_opy_ (u"ࠧࡩࡱࡲ࡯ࠬἥ"))
    def bstack1l11ll11_opy_(self):
        return self.hook_type
    def bstack11111l1111l_opy_(self):
        return {
            bstack1ll1ll1_opy_ (u"ࠨࡪࡲࡳࡰࡥࡴࡺࡲࡨࠫἦ"): self.hook_type
        }
    def bstack11111l1l111_opy_(self):
        return {
            **super().bstack11111l1l111_opy_(),
            **self.bstack11111l1111l_opy_()
        }
    def bstack111111lllll_opy_(self):
        return {
            **super().bstack111111lllll_opy_(),
            bstack1ll1ll1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣ࡮ࡪࠧἧ"): self.bstack1l111llllll_opy_,
            **self.bstack11111l1111l_opy_()
        }
    def event_key(self):
        return bstack1ll1ll1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࠬἨ")
    def bstack11l1lll1_opy_(self, bstack1l111llllll_opy_):
        self.bstack1l111llllll_opy_ = bstack1l111llllll_opy_