# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
import os
from uuid import uuid4
from bstack_utils.helper import bstack1ll11l1l_opy_, bstack111ll11111l_opy_
from bstack_utils.bstack11llllll1_opy_ import bstack11l11l11l1l_opy_
class bstack1l1111l1_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, started_at=None, framework=None, tags=[], scope=[], bstack11111l1l11l_opy_=None, bstack111111lll1l_opy_=True, bstack1ll1l1lllll_opy_=None, bstack1l1llllll1_opy_=None, result=None, duration=None, bstack1ll11lll_opy_=None, meta={}):
        self.bstack1ll11lll_opy_ = bstack1ll11lll_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack111111lll1l_opy_:
            self.uuid = uuid4().__str__()
        self.started_at = started_at
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack11111l1l11l_opy_ = bstack11111l1l11l_opy_
        self.bstack1ll1l1lllll_opy_ = bstack1ll1l1lllll_opy_
        self.bstack1l1llllll1_opy_ = bstack1l1llllll1_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
        self.hooks = []
    def bstack1l11ll11_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack11ll1l1l_opy_(self, meta):
        self.meta = meta
    def bstack11l1l1l1_opy_(self, hooks):
        self.hooks = hooks
    def bstack111111ll1ll_opy_(self):
        bstack111111llll1_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack1l_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧỪ"): bstack111111llll1_opy_,
            bstack1l_opy_ (u"ࠬࡲ࡯ࡤࡣࡷ࡭ࡴࡴࠧừ"): bstack111111llll1_opy_,
            bstack1l_opy_ (u"࠭ࡶࡤࡡࡩ࡭ࡱ࡫ࡰࡢࡶ࡫ࠫỬ"): bstack111111llll1_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack1l_opy_ (u"ࠢࡖࡰࡨࡼࡵ࡫ࡣࡵࡧࡧࠤࡦࡸࡧࡶ࡯ࡨࡲࡹࡀࠠࠣử") + key)
            setattr(self, key, val)
    def bstack11111l11ll1_opy_(self):
        return {
            bstack1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭Ữ"): self.name,
            bstack1l_opy_ (u"ࠩࡥࡳࡩࡿࠧữ"): {
                bstack1l_opy_ (u"ࠪࡰࡦࡴࡧࠨỰ"): bstack1l_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫự"),
                bstack1l_opy_ (u"ࠬࡩ࡯ࡥࡧࠪỲ"): self.code
            },
            bstack1l_opy_ (u"࠭ࡳࡤࡱࡳࡩࡸ࠭ỳ"): self.scope,
            bstack1l_opy_ (u"ࠧࡵࡣࡪࡷࠬỴ"): self.tags,
            bstack1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫỵ"): self.framework,
            bstack1l_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭Ỷ"): self.started_at
        }
    def bstack11111l1l1l1_opy_(self):
        return {
         bstack1l_opy_ (u"ࠪࡱࡪࡺࡡࠨỷ"): self.meta
        }
    def bstack11111l1l1ll_opy_(self):
        return {
            bstack1l_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡖࡪࡸࡵ࡯ࡒࡤࡶࡦࡳࠧỸ"): {
                bstack1l_opy_ (u"ࠬࡸࡥࡳࡷࡱࡣࡳࡧ࡭ࡦࠩỹ"): self.bstack11111l1l11l_opy_
            }
        }
    def bstack111111lllll_opy_(self, bstack11111l1l111_opy_, details):
        step = next(filter(lambda st: st[bstack1l_opy_ (u"࠭ࡩࡥࠩỺ")] == bstack11111l1l111_opy_, self.meta[bstack1l_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ỻ")]), None)
        step.update(details)
    def bstack11ll11ll_opy_(self, bstack11111l1l111_opy_):
        step = next(filter(lambda st: st[bstack1l_opy_ (u"ࠨ࡫ࡧࠫỼ")] == bstack11111l1l111_opy_, self.meta[bstack1l_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨỽ")]), None)
        step.update({
            bstack1l_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧỾ"): bstack1ll11l1l_opy_()
        })
    def bstack1l11lll1_opy_(self, bstack11111l1l111_opy_, result, duration=None):
        bstack1ll1l1lllll_opy_ = bstack1ll11l1l_opy_()
        if bstack11111l1l111_opy_ is not None and self.meta.get(bstack1l_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪỿ")):
            step = next(filter(lambda st: st[bstack1l_opy_ (u"ࠬ࡯ࡤࠨἀ")] == bstack11111l1l111_opy_, self.meta[bstack1l_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬἁ")]), None)
            step.update({
                bstack1l_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬἂ"): bstack1ll1l1lllll_opy_,
                bstack1l_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࠪἃ"): duration if duration else bstack111ll11111l_opy_(step[bstack1l_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ἄ")], bstack1ll1l1lllll_opy_),
                bstack1l_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪἅ"): result.result,
                bstack1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬἆ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack11111l1111l_opy_):
        if self.meta.get(bstack1l_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫἇ")):
            self.meta[bstack1l_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬἈ")].append(bstack11111l1111l_opy_)
        else:
            self.meta[bstack1l_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭Ἁ")] = [ bstack11111l1111l_opy_ ]
    def bstack11111l11l11_opy_(self):
        return {
            bstack1l_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭Ἂ"): self.bstack1l11ll11_opy_(),
            **self.bstack11111l11ll1_opy_(),
            **self.bstack111111ll1ll_opy_(),
            **self.bstack11111l1l1l1_opy_()
        }
    def bstack111111lll11_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack1l_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧἋ"): self.bstack1ll1l1lllll_opy_,
            bstack1l_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࡤ࡯࡮ࡠ࡯ࡶࠫἌ"): self.duration,
            bstack1l_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫἍ"): self.result.result
        }
        if data[bstack1l_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬἎ")] == bstack1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭Ἇ"):
            data[bstack1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࡠࡶࡼࡴࡪ࠭ἐ")] = self.result.bstack11111l11ll_opy_()
            data[bstack1l_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩἑ")] = [{bstack1l_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬἒ"): self.result.bstack111l1l1l1ll_opy_()}]
        return data
    def bstack11111l11111_opy_(self):
        return {
            bstack1l_opy_ (u"ࠪࡹࡺ࡯ࡤࠨἓ"): self.bstack1l11ll11_opy_(),
            **self.bstack11111l11ll1_opy_(),
            **self.bstack111111ll1ll_opy_(),
            **self.bstack111111lll11_opy_(),
            **self.bstack11111l1l1l1_opy_()
        }
    def bstack1l111l11_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack1l_opy_ (u"ࠫࡘࡺࡡࡳࡶࡨࡨࠬἔ") in event:
            return self.bstack11111l11l11_opy_()
        elif bstack1l_opy_ (u"ࠬࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧἕ") in event:
            return self.bstack11111l11111_opy_()
    def event_key(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1ll1l1lllll_opy_ = time if time else bstack1ll11l1l_opy_()
        self.duration = duration if duration else bstack111ll11111l_opy_(self.started_at, self.bstack1ll1l1lllll_opy_)
        if result:
            self.result = result
class bstack1ll1l1ll_opy_(bstack1l1111l1_opy_):
    def __init__(self, hooks=[], bstack1l1l11ll_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack1l1l11ll_opy_ = bstack1l1l11ll_opy_
        super().__init__(*args, **kwargs, bstack1l1llllll1_opy_=bstack1l_opy_ (u"࠭ࡴࡦࡵࡷࠫ἖"))
    @classmethod
    def bstack11111l111l1_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack1l_opy_ (u"ࠧࡪࡦࠪ἗"): id(step),
                bstack1l_opy_ (u"ࠨࡶࡨࡼࡹ࠭Ἐ"): step.name,
                bstack1l_opy_ (u"ࠩ࡮ࡩࡾࡽ࡯ࡳࡦࠪἙ"): step.keyword,
            })
        return bstack1ll1l1ll_opy_(
            **kwargs,
            meta={
                bstack1l_opy_ (u"ࠪࡪࡪࡧࡴࡶࡴࡨࠫἚ"): {
                    bstack1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩἛ"): feature.name,
                    bstack1l_opy_ (u"ࠬࡶࡡࡵࡪࠪἜ"): feature.filename,
                    bstack1l_opy_ (u"࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫἝ"): feature.description
                },
                bstack1l_opy_ (u"ࠧࡴࡥࡨࡲࡦࡸࡩࡰࠩ἞"): {
                    bstack1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭἟"): scenario.name
                },
                bstack1l_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨἠ"): steps,
                bstack1l_opy_ (u"ࠪࡩࡽࡧ࡭ࡱ࡮ࡨࡷࠬἡ"): bstack11l11l11l1l_opy_(test)
            }
        )
    def bstack11111l11l1l_opy_(self):
        return {
            bstack1l_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪἢ"): self.hooks
        }
    def bstack11111l11lll_opy_(self):
        if self.bstack1l1l11ll_opy_:
            return {
                bstack1l_opy_ (u"ࠬ࡯࡮ࡵࡧࡪࡶࡦࡺࡩࡰࡰࡶࠫἣ"): self.bstack1l1l11ll_opy_
            }
        return {}
    def bstack11111l11111_opy_(self):
        return {
            **super().bstack11111l11111_opy_(),
            **self.bstack11111l11l1l_opy_()
        }
    def bstack11111l11l11_opy_(self):
        return {
            **super().bstack11111l11l11_opy_(),
            **self.bstack11111l11lll_opy_()
        }
    def event_key(self):
        return bstack1l_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࠨἤ")
class bstack11lllll1_opy_(bstack1l1111l1_opy_):
    def __init__(self, hook_type, *args,bstack1l1l11ll_opy_={}, **kwargs):
        self.hook_type = hook_type
        self.bstack1l1111ll1l1_opy_ = None
        self.bstack1l1l11ll_opy_ = bstack1l1l11ll_opy_
        super().__init__(*args, **kwargs, bstack1l1llllll1_opy_=bstack1l_opy_ (u"ࠧࡩࡱࡲ࡯ࠬἥ"))
    def bstack1ll1l11l_opy_(self):
        return self.hook_type
    def bstack11111l111ll_opy_(self):
        return {
            bstack1l_opy_ (u"ࠨࡪࡲࡳࡰࡥࡴࡺࡲࡨࠫἦ"): self.hook_type
        }
    def bstack11111l11111_opy_(self):
        return {
            **super().bstack11111l11111_opy_(),
            **self.bstack11111l111ll_opy_()
        }
    def bstack11111l11l11_opy_(self):
        return {
            **super().bstack11111l11l11_opy_(),
            bstack1l_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣ࡮ࡪࠧἧ"): self.bstack1l1111ll1l1_opy_,
            **self.bstack11111l111ll_opy_()
        }
    def event_key(self):
        return bstack1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࠬἨ")
    def bstack11l1l1ll_opy_(self, bstack1l1111ll1l1_opy_):
        self.bstack1l1111ll1l1_opy_ = bstack1l1111ll1l1_opy_