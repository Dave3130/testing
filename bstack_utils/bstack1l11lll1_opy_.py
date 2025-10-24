# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
import os
from uuid import uuid4
from bstack_utils.helper import bstack1l1ll11l_opy_, bstack1111llll1ll_opy_
from bstack_utils.bstack1l1l1l1ll_opy_ import bstack11l111ll11l_opy_
class bstack1ll1ll11_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, started_at=None, framework=None, tags=[], scope=[], bstack111111lll11_opy_=None, bstack111111l1lll_opy_=True, bstack1ll11lll111_opy_=None, bstack11ll11l11_opy_=None, result=None, duration=None, bstack1l1l1111_opy_=None, meta={}):
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
        self.bstack111111lll11_opy_ = bstack111111lll11_opy_
        self.bstack1ll11lll111_opy_ = bstack1ll11lll111_opy_
        self.bstack11ll11l11_opy_ = bstack11ll11l11_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
        self.hooks = []
    def bstack1l11ll1l_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack11l1l11l_opy_(self, meta):
        self.meta = meta
    def bstack11l11ll1_opy_(self, hooks):
        self.hooks = hooks
    def bstack11111l1111l_opy_(self):
        bstack11111l111l1_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack1l1_opy_ (u"ࠫ࡫࡯࡬ࡦࡡࡱࡥࡲ࡫ࠧỿ"): bstack11111l111l1_opy_,
            bstack1l1_opy_ (u"ࠬࡲ࡯ࡤࡣࡷ࡭ࡴࡴࠧἀ"): bstack11111l111l1_opy_,
            bstack1l1_opy_ (u"࠭ࡶࡤࡡࡩ࡭ࡱ࡫ࡰࡢࡶ࡫ࠫἁ"): bstack11111l111l1_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack1l1_opy_ (u"ࠢࡖࡰࡨࡼࡵ࡫ࡣࡵࡧࡧࠤࡦࡸࡧࡶ࡯ࡨࡲࡹࡀࠠࠣἂ") + key)
            setattr(self, key, val)
    def bstack111111l1l1l_opy_(self):
        return {
            bstack1l1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ἃ"): self.name,
            bstack1l1_opy_ (u"ࠩࡥࡳࡩࡿࠧἄ"): {
                bstack1l1_opy_ (u"ࠪࡰࡦࡴࡧࠨἅ"): bstack1l1_opy_ (u"ࠫࡵࡿࡴࡩࡱࡱࠫἆ"),
                bstack1l1_opy_ (u"ࠬࡩ࡯ࡥࡧࠪἇ"): self.code
            },
            bstack1l1_opy_ (u"࠭ࡳࡤࡱࡳࡩࡸ࠭Ἀ"): self.scope,
            bstack1l1_opy_ (u"ࠧࡵࡣࡪࡷࠬἉ"): self.tags,
            bstack1l1_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫἊ"): self.framework,
            bstack1l1_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭Ἃ"): self.started_at
        }
    def bstack11111l11111_opy_(self):
        return {
         bstack1l1_opy_ (u"ࠪࡱࡪࡺࡡࠨἌ"): self.meta
        }
    def bstack111111l11l1_opy_(self):
        return {
            bstack1l1_opy_ (u"ࠫࡨࡻࡳࡵࡱࡰࡖࡪࡸࡵ࡯ࡒࡤࡶࡦࡳࠧἍ"): {
                bstack1l1_opy_ (u"ࠬࡸࡥࡳࡷࡱࡣࡳࡧ࡭ࡦࠩἎ"): self.bstack111111lll11_opy_
            }
        }
    def bstack111111ll1ll_opy_(self, bstack111111l1l11_opy_, details):
        step = next(filter(lambda st: st[bstack1l1_opy_ (u"࠭ࡩࡥࠩἏ")] == bstack111111l1l11_opy_, self.meta[bstack1l1_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭ἐ")]), None)
        step.update(details)
    def bstack11l11l11_opy_(self, bstack111111l1l11_opy_):
        step = next(filter(lambda st: st[bstack1l1_opy_ (u"ࠨ࡫ࡧࠫἑ")] == bstack111111l1l11_opy_, self.meta[bstack1l1_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨἒ")]), None)
        step.update({
            bstack1l1_opy_ (u"ࠪࡷࡹࡧࡲࡵࡧࡧࡣࡦࡺࠧἓ"): bstack1l1ll11l_opy_()
        })
    def bstack1lll1lll_opy_(self, bstack111111l1l11_opy_, result, duration=None):
        bstack1ll11lll111_opy_ = bstack1l1ll11l_opy_()
        if bstack111111l1l11_opy_ is not None and self.meta.get(bstack1l1_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪἔ")):
            step = next(filter(lambda st: st[bstack1l1_opy_ (u"ࠬ࡯ࡤࠨἕ")] == bstack111111l1l11_opy_, self.meta[bstack1l1_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬ἖")]), None)
            step.update({
                bstack1l1_opy_ (u"ࠧࡧ࡫ࡱ࡭ࡸ࡮ࡥࡥࡡࡤࡸࠬ἗"): bstack1ll11lll111_opy_,
                bstack1l1_opy_ (u"ࠨࡦࡸࡶࡦࡺࡩࡰࡰࠪἘ"): duration if duration else bstack1111llll1ll_opy_(step[bstack1l1_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭Ἑ")], bstack1ll11lll111_opy_),
                bstack1l1_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪἚ"): result.result,
                bstack1l1_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࠬἛ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack111111ll111_opy_):
        if self.meta.get(bstack1l1_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫἜ")):
            self.meta[bstack1l1_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬἝ")].append(bstack111111ll111_opy_)
        else:
            self.meta[bstack1l1_opy_ (u"ࠧࡴࡶࡨࡴࡸ࠭἞")] = [ bstack111111ll111_opy_ ]
    def bstack111111ll11l_opy_(self):
        return {
            bstack1l1_opy_ (u"ࠨࡷࡸ࡭ࡩ࠭἟"): self.bstack1l11ll1l_opy_(),
            **self.bstack111111l1l1l_opy_(),
            **self.bstack11111l1111l_opy_(),
            **self.bstack11111l11111_opy_()
        }
    def bstack111111lllll_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack1l1_opy_ (u"ࠩࡩ࡭ࡳ࡯ࡳࡩࡧࡧࡣࡦࡺࠧἠ"): self.bstack1ll11lll111_opy_,
            bstack1l1_opy_ (u"ࠪࡨࡺࡸࡡࡵ࡫ࡲࡲࡤ࡯࡮ࡠ࡯ࡶࠫἡ"): self.duration,
            bstack1l1_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫἢ"): self.result.result
        }
        if data[bstack1l1_opy_ (u"ࠬࡸࡥࡴࡷ࡯ࡸࠬἣ")] == bstack1l1_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ἤ"):
            data[bstack1l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࡠࡶࡼࡴࡪ࠭ἥ")] = self.result.bstack111111l111_opy_()
            data[bstack1l1_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩἦ")] = [{bstack1l1_opy_ (u"ࠩࡥࡥࡨࡱࡴࡳࡣࡦࡩࠬἧ"): self.result.bstack111l11111l1_opy_()}]
        return data
    def bstack111111lll1l_opy_(self):
        return {
            bstack1l1_opy_ (u"ࠪࡹࡺ࡯ࡤࠨἨ"): self.bstack1l11ll1l_opy_(),
            **self.bstack111111l1l1l_opy_(),
            **self.bstack11111l1111l_opy_(),
            **self.bstack111111lllll_opy_(),
            **self.bstack11111l11111_opy_()
        }
    def bstack1ll11ll1_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack1l1_opy_ (u"ࠫࡘࡺࡡࡳࡶࡨࡨࠬἩ") in event:
            return self.bstack111111ll11l_opy_()
        elif bstack1l1_opy_ (u"ࠬࡌࡩ࡯࡫ࡶ࡬ࡪࡪࠧἪ") in event:
            return self.bstack111111lll1l_opy_()
    def event_key(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1ll11lll111_opy_ = time if time else bstack1l1ll11l_opy_()
        self.duration = duration if duration else bstack1111llll1ll_opy_(self.started_at, self.bstack1ll11lll111_opy_)
        if result:
            self.result = result
class bstack1lll1l1l_opy_(bstack1ll1ll11_opy_):
    def __init__(self, hooks=[], bstack1lll11l1_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack1lll11l1_opy_ = bstack1lll11l1_opy_
        super().__init__(*args, **kwargs, bstack11ll11l11_opy_=bstack1l1_opy_ (u"࠭ࡴࡦࡵࡷࠫἫ"))
    @classmethod
    def bstack111111l11ll_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack1l1_opy_ (u"ࠧࡪࡦࠪἬ"): id(step),
                bstack1l1_opy_ (u"ࠨࡶࡨࡼࡹ࠭Ἥ"): step.name,
                bstack1l1_opy_ (u"ࠩ࡮ࡩࡾࡽ࡯ࡳࡦࠪἮ"): step.keyword,
            })
        return bstack1lll1l1l_opy_(
            **kwargs,
            meta={
                bstack1l1_opy_ (u"ࠪࡪࡪࡧࡴࡶࡴࡨࠫἯ"): {
                    bstack1l1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩἰ"): feature.name,
                    bstack1l1_opy_ (u"ࠬࡶࡡࡵࡪࠪἱ"): feature.filename,
                    bstack1l1_opy_ (u"࠭ࡤࡦࡵࡦࡶ࡮ࡶࡴࡪࡱࡱࠫἲ"): feature.description
                },
                bstack1l1_opy_ (u"ࠧࡴࡥࡨࡲࡦࡸࡩࡰࠩἳ"): {
                    bstack1l1_opy_ (u"ࠨࡰࡤࡱࡪ࠭ἴ"): scenario.name
                },
                bstack1l1_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨἵ"): steps,
                bstack1l1_opy_ (u"ࠪࡩࡽࡧ࡭ࡱ࡮ࡨࡷࠬἶ"): bstack11l111ll11l_opy_(test)
            }
        )
    def bstack111111llll1_opy_(self):
        return {
            bstack1l1_opy_ (u"ࠫ࡭ࡵ࡯࡬ࡵࠪἷ"): self.hooks
        }
    def bstack111111l1ll1_opy_(self):
        if self.bstack1lll11l1_opy_:
            return {
                bstack1l1_opy_ (u"ࠬ࡯࡮ࡵࡧࡪࡶࡦࡺࡩࡰࡰࡶࠫἸ"): self.bstack1lll11l1_opy_
            }
        return {}
    def bstack111111lll1l_opy_(self):
        return {
            **super().bstack111111lll1l_opy_(),
            **self.bstack111111llll1_opy_()
        }
    def bstack111111ll11l_opy_(self):
        return {
            **super().bstack111111ll11l_opy_(),
            **self.bstack111111l1ll1_opy_()
        }
    def event_key(self):
        return bstack1l1_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࠨἹ")
class bstack1ll1111l_opy_(bstack1ll1ll11_opy_):
    def __init__(self, hook_type, *args,bstack1lll11l1_opy_={}, **kwargs):
        self.hook_type = hook_type
        self.bstack1l1111l1l1l_opy_ = None
        self.bstack1lll11l1_opy_ = bstack1lll11l1_opy_
        super().__init__(*args, **kwargs, bstack11ll11l11_opy_=bstack1l1_opy_ (u"ࠧࡩࡱࡲ࡯ࠬἺ"))
    def bstack1lllll11_opy_(self):
        return self.hook_type
    def bstack111111ll1l1_opy_(self):
        return {
            bstack1l1_opy_ (u"ࠨࡪࡲࡳࡰࡥࡴࡺࡲࡨࠫἻ"): self.hook_type
        }
    def bstack111111lll1l_opy_(self):
        return {
            **super().bstack111111lll1l_opy_(),
            **self.bstack111111ll1l1_opy_()
        }
    def bstack111111ll11l_opy_(self):
        return {
            **super().bstack111111ll11l_opy_(),
            bstack1l1_opy_ (u"ࠩࡷࡩࡸࡺ࡟ࡳࡷࡱࡣ࡮ࡪࠧἼ"): self.bstack1l1111l1l1l_opy_,
            **self.bstack111111ll1l1_opy_()
        }
    def event_key(self):
        return bstack1l1_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡠࡴࡸࡲࠬἽ")
    def bstack11l1l1ll_opy_(self, bstack1l1111l1l1l_opy_):
        self.bstack1l1111l1l1l_opy_ = bstack1l1111l1l1l_opy_