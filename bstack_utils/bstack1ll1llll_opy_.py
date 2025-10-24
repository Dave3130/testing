# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
import os
from uuid import uuid4
from bstack_utils.helper import bstack1l11ll1l_opy_, bstack1111lllllll_opy_
from bstack_utils.bstack11l111l111_opy_ import bstack11l111ll1l1_opy_
class bstack1l11ll11_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, started_at=None, framework=None, tags=[], scope=[], bstack111111l1ll1_opy_=None, bstack11111l111l1_opy_=True, bstack1l1lll1llll_opy_=None, bstack1l1l1l11l1_opy_=None, result=None, duration=None, bstack1lllll11_opy_=None, meta={}):
        self.bstack1lllll11_opy_ = bstack1lllll11_opy_
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
        self.bstack111111l1ll1_opy_ = bstack111111l1ll1_opy_
        self.bstack1l1lll1llll_opy_ = bstack1l1lll1llll_opy_
        self.bstack1l1l1l11l1_opy_ = bstack1l1l1l11l1_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
        self.hooks = []
    def bstack1ll1l111_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack11l11l1l_opy_(self, meta):
        self.meta = meta
    def bstack11l11ll1_opy_(self, hooks):
        self.hooks = hooks
    def bstack111111lllll_opy_(self):
        bstack11111l1111l_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack11l11l1_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭Ỿ"): bstack11111l1111l_opy_,
            bstack11l11l1_opy_ (u"ࠫࡱࡵࡣࡢࡶ࡬ࡳࡳ࠭ỿ"): bstack11111l1111l_opy_,
            bstack11l11l1_opy_ (u"ࠬࡼࡣࡠࡨ࡬ࡰࡪࡶࡡࡵࡪࠪἀ"): bstack11111l1111l_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack11l11l1_opy_ (u"ࠨࡕ࡯ࡧࡻࡴࡪࡩࡴࡦࡦࠣࡥࡷ࡭ࡵ࡮ࡧࡱࡸ࠿ࠦࠢἁ") + key)
            setattr(self, key, val)
    def bstack111111l11l1_opy_(self):
        return {
            bstack11l11l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬἂ"): self.name,
            bstack11l11l1_opy_ (u"ࠨࡤࡲࡨࡾ࠭ἃ"): {
                bstack11l11l1_opy_ (u"ࠩ࡯ࡥࡳ࡭ࠧἄ"): bstack11l11l1_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪἅ"),
                bstack11l11l1_opy_ (u"ࠫࡨࡵࡤࡦࠩἆ"): self.code
            },
            bstack11l11l1_opy_ (u"ࠬࡹࡣࡰࡲࡨࡷࠬἇ"): self.scope,
            bstack11l11l1_opy_ (u"࠭ࡴࡢࡩࡶࠫἈ"): self.tags,
            bstack11l11l1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪἉ"): self.framework,
            bstack11l11l1_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬἊ"): self.started_at
        }
    def bstack111111l1l1l_opy_(self):
        return {
         bstack11l11l1_opy_ (u"ࠩࡰࡩࡹࡧࠧἋ"): self.meta
        }
    def bstack111111llll1_opy_(self):
        return {
            bstack11l11l1_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡕࡩࡷࡻ࡮ࡑࡣࡵࡥࡲ࠭Ἄ"): {
                bstack11l11l1_opy_ (u"ࠫࡷ࡫ࡲࡶࡰࡢࡲࡦࡳࡥࠨἍ"): self.bstack111111l1ll1_opy_
            }
        }
    def bstack111111lll11_opy_(self, bstack111111ll1ll_opy_, details):
        step = next(filter(lambda st: st[bstack11l11l1_opy_ (u"ࠬ࡯ࡤࠨἎ")] == bstack111111ll1ll_opy_, self.meta[bstack11l11l1_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬἏ")]), None)
        step.update(details)
    def bstack11l11l11_opy_(self, bstack111111ll1ll_opy_):
        step = next(filter(lambda st: st[bstack11l11l1_opy_ (u"ࠧࡪࡦࠪἐ")] == bstack111111ll1ll_opy_, self.meta[bstack11l11l1_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧἑ")]), None)
        step.update({
            bstack11l11l1_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭ἒ"): bstack1l11ll1l_opy_()
        })
    def bstack1l1ll1ll_opy_(self, bstack111111ll1ll_opy_, result, duration=None):
        bstack1l1lll1llll_opy_ = bstack1l11ll1l_opy_()
        if bstack111111ll1ll_opy_ is not None and self.meta.get(bstack11l11l1_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩἓ")):
            step = next(filter(lambda st: st[bstack11l11l1_opy_ (u"ࠫ࡮ࡪࠧἔ")] == bstack111111ll1ll_opy_, self.meta[bstack11l11l1_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫἕ")]), None)
            step.update({
                bstack11l11l1_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫ἖"): bstack1l1lll1llll_opy_,
                bstack11l11l1_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࠩ἗"): duration if duration else bstack1111lllllll_opy_(step[bstack11l11l1_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬἘ")], bstack1l1lll1llll_opy_),
                bstack11l11l1_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩἙ"): result.result,
                bstack11l11l1_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫἚ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack111111ll1l1_opy_):
        if self.meta.get(bstack11l11l1_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪἛ")):
            self.meta[bstack11l11l1_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫἜ")].append(bstack111111ll1l1_opy_)
        else:
            self.meta[bstack11l11l1_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬἝ")] = [ bstack111111ll1l1_opy_ ]
    def bstack111111l11ll_opy_(self):
        return {
            bstack11l11l1_opy_ (u"ࠧࡶࡷ࡬ࡨࠬ἞"): self.bstack1ll1l111_opy_(),
            **self.bstack111111l11l1_opy_(),
            **self.bstack111111lllll_opy_(),
            **self.bstack111111l1l1l_opy_()
        }
    def bstack111111ll111_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack11l11l1_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭἟"): self.bstack1l1lll1llll_opy_,
            bstack11l11l1_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࡣ࡮ࡴ࡟࡮ࡵࠪἠ"): self.duration,
            bstack11l11l1_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪἡ"): self.result.result
        }
        if data[bstack11l11l1_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫἢ")] == bstack11l11l1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬἣ"):
            data[bstack11l11l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫࡟ࡵࡻࡳࡩࠬἤ")] = self.result.bstack111111l1ll_opy_()
            data[bstack11l11l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨἥ")] = [{bstack11l11l1_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫἦ"): self.result.bstack111l1ll1l11_opy_()}]
        return data
    def bstack111111lll1l_opy_(self):
        return {
            bstack11l11l1_opy_ (u"ࠩࡸࡹ࡮ࡪࠧἧ"): self.bstack1ll1l111_opy_(),
            **self.bstack111111l11l1_opy_(),
            **self.bstack111111lllll_opy_(),
            **self.bstack111111ll111_opy_(),
            **self.bstack111111l1l1l_opy_()
        }
    def bstack11lll11l_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack11l11l1_opy_ (u"ࠪࡗࡹࡧࡲࡵࡧࡧࠫἨ") in event:
            return self.bstack111111l11ll_opy_()
        elif bstack11l11l1_opy_ (u"ࠫࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭Ἡ") in event:
            return self.bstack111111lll1l_opy_()
    def event_key(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1l1lll1llll_opy_ = time if time else bstack1l11ll1l_opy_()
        self.duration = duration if duration else bstack1111lllllll_opy_(self.started_at, self.bstack1l1lll1llll_opy_)
        if result:
            self.result = result
class bstack11llll1l_opy_(bstack1l11ll11_opy_):
    def __init__(self, hooks=[], bstack1llll11l_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack1llll11l_opy_ = bstack1llll11l_opy_
        super().__init__(*args, **kwargs, bstack1l1l1l11l1_opy_=bstack11l11l1_opy_ (u"ࠬࡺࡥࡴࡶࠪἪ"))
    @classmethod
    def bstack111111ll11l_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack11l11l1_opy_ (u"࠭ࡩࡥࠩἫ"): id(step),
                bstack11l11l1_opy_ (u"ࠧࡵࡧࡻࡸࠬἬ"): step.name,
                bstack11l11l1_opy_ (u"ࠨ࡭ࡨࡽࡼࡵࡲࡥࠩἭ"): step.keyword,
            })
        return bstack11llll1l_opy_(
            **kwargs,
            meta={
                bstack11l11l1_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࠪἮ"): {
                    bstack11l11l1_opy_ (u"ࠪࡲࡦࡳࡥࠨἯ"): feature.name,
                    bstack11l11l1_opy_ (u"ࠫࡵࡧࡴࡩࠩἰ"): feature.filename,
                    bstack11l11l1_opy_ (u"ࠬࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪἱ"): feature.description
                },
                bstack11l11l1_opy_ (u"࠭ࡳࡤࡧࡱࡥࡷ࡯࡯ࠨἲ"): {
                    bstack11l11l1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬἳ"): scenario.name
                },
                bstack11l11l1_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧἴ"): steps,
                bstack11l11l1_opy_ (u"ࠩࡨࡼࡦࡳࡰ࡭ࡧࡶࠫἵ"): bstack11l111ll1l1_opy_(test)
            }
        )
    def bstack11111l11111_opy_(self):
        return {
            bstack11l11l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩἶ"): self.hooks
        }
    def bstack111111l1lll_opy_(self):
        if self.bstack1llll11l_opy_:
            return {
                bstack11l11l1_opy_ (u"ࠫ࡮ࡴࡴࡦࡩࡵࡥࡹ࡯࡯࡯ࡵࠪἷ"): self.bstack1llll11l_opy_
            }
        return {}
    def bstack111111lll1l_opy_(self):
        return {
            **super().bstack111111lll1l_opy_(),
            **self.bstack11111l11111_opy_()
        }
    def bstack111111l11ll_opy_(self):
        return {
            **super().bstack111111l11ll_opy_(),
            **self.bstack111111l1lll_opy_()
        }
    def event_key(self):
        return bstack11l11l1_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧἸ")
class bstack1l1llll1_opy_(bstack1l11ll11_opy_):
    def __init__(self, hook_type, *args,bstack1llll11l_opy_={}, **kwargs):
        self.hook_type = hook_type
        self.bstack1l111l11ll1_opy_ = None
        self.bstack1llll11l_opy_ = bstack1llll11l_opy_
        super().__init__(*args, **kwargs, bstack1l1l1l11l1_opy_=bstack11l11l1_opy_ (u"࠭ࡨࡰࡱ࡮ࠫἹ"))
    def bstack1ll1111l_opy_(self):
        return self.hook_type
    def bstack111111l1l11_opy_(self):
        return {
            bstack11l11l1_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧࠪἺ"): self.hook_type
        }
    def bstack111111lll1l_opy_(self):
        return {
            **super().bstack111111lll1l_opy_(),
            **self.bstack111111l1l11_opy_()
        }
    def bstack111111l11ll_opy_(self):
        return {
            **super().bstack111111l11ll_opy_(),
            bstack11l11l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢ࡭ࡩ࠭Ἳ"): self.bstack1l111l11ll1_opy_,
            **self.bstack111111l1l11_opy_()
        }
    def event_key(self):
        return bstack11l11l1_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࠫἼ")
    def bstack11l1lll1_opy_(self, bstack1l111l11ll1_opy_):
        self.bstack1l111l11ll1_opy_ = bstack1l111l11ll1_opy_