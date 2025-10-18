# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
from uuid import uuid4
from bstack_utils.helper import bstack11lllll1_opy_, bstack1111l11llll_opy_
from bstack_utils.bstack1l11lll1l_opy_ import bstack11l111l11l1_opy_
class bstack1l1l11ll_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, started_at=None, framework=None, tags=[], scope=[], bstack111111l1l11_opy_=None, bstack111111ll111_opy_=True, bstack1ll1l1ll11l_opy_=None, bstack1ll111111l_opy_=None, result=None, duration=None, bstack1l11l1ll_opy_=None, meta={}):
        self.bstack1l11l1ll_opy_ = bstack1l11l1ll_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack111111ll111_opy_:
            self.uuid = uuid4().__str__()
        self.started_at = started_at
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack111111l1l11_opy_ = bstack111111l1l11_opy_
        self.bstack1ll1l1ll11l_opy_ = bstack1ll1l1ll11l_opy_
        self.bstack1ll111111l_opy_ = bstack1ll111111l_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
        self.hooks = []
    def bstack1l1l1ll1_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack11l11lll_opy_(self, meta):
        self.meta = meta
    def bstack11l11ll1_opy_(self, hooks):
        self.hooks = hooks
    def bstack111111ll11l_opy_(self):
        bstack11111l11111_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack11l111_opy_ (u"ࠨࡨ࡬ࡰࡪࡥ࡮ࡢ࡯ࡨࠫἊ"): bstack11111l11111_opy_,
            bstack11l111_opy_ (u"ࠩ࡯ࡳࡨࡧࡴࡪࡱࡱࠫἋ"): bstack11111l11111_opy_,
            bstack11l111_opy_ (u"ࠪࡺࡨࡥࡦࡪ࡮ࡨࡴࡦࡺࡨࠨἌ"): bstack11111l11111_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack11l111_opy_ (u"࡚ࠦࡴࡥࡹࡲࡨࡧࡹ࡫ࡤࠡࡣࡵ࡫ࡺࡳࡥ࡯ࡶ࠽ࠤࠧἍ") + key)
            setattr(self, key, val)
    def bstack111111l11l1_opy_(self):
        return {
            bstack11l111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪἎ"): self.name,
            bstack11l111_opy_ (u"࠭ࡢࡰࡦࡼࠫἏ"): {
                bstack11l111_opy_ (u"ࠧ࡭ࡣࡱ࡫ࠬἐ"): bstack11l111_opy_ (u"ࠨࡲࡼࡸ࡭ࡵ࡮ࠨἑ"),
                bstack11l111_opy_ (u"ࠩࡦࡳࡩ࡫ࠧἒ"): self.code
            },
            bstack11l111_opy_ (u"ࠪࡷࡨࡵࡰࡦࡵࠪἓ"): self.scope,
            bstack11l111_opy_ (u"ࠫࡹࡧࡧࡴࠩἔ"): self.tags,
            bstack11l111_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨἕ"): self.framework,
            bstack11l111_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪ἖"): self.started_at
        }
    def bstack111111llll1_opy_(self):
        return {
         bstack11l111_opy_ (u"ࠧ࡮ࡧࡷࡥࠬ἗"): self.meta
        }
    def bstack111111l1ll1_opy_(self):
        return {
            bstack11l111_opy_ (u"ࠨࡥࡸࡷࡹࡵ࡭ࡓࡧࡵࡹࡳࡖࡡࡳࡣࡰࠫἘ"): {
                bstack11l111_opy_ (u"ࠩࡵࡩࡷࡻ࡮ࡠࡰࡤࡱࡪ࠭Ἑ"): self.bstack111111l1l11_opy_
            }
        }
    def bstack111111l11ll_opy_(self, bstack111111l1lll_opy_, details):
        step = next(filter(lambda st: st[bstack11l111_opy_ (u"ࠪ࡭ࡩ࠭Ἒ")] == bstack111111l1lll_opy_, self.meta[bstack11l111_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪἛ")]), None)
        step.update(details)
    def bstack11l1l1l1_opy_(self, bstack111111l1lll_opy_):
        step = next(filter(lambda st: st[bstack11l111_opy_ (u"ࠬ࡯ࡤࠨἜ")] == bstack111111l1lll_opy_, self.meta[bstack11l111_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬἝ")]), None)
        step.update({
            bstack11l111_opy_ (u"ࠧࡴࡶࡤࡶࡹ࡫ࡤࡠࡣࡷࠫ἞"): bstack11lllll1_opy_()
        })
    def bstack1l1l11l1_opy_(self, bstack111111l1lll_opy_, result, duration=None):
        bstack1ll1l1ll11l_opy_ = bstack11lllll1_opy_()
        if bstack111111l1lll_opy_ is not None and self.meta.get(bstack11l111_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧ἟")):
            step = next(filter(lambda st: st[bstack11l111_opy_ (u"ࠩ࡬ࡨࠬἠ")] == bstack111111l1lll_opy_, self.meta[bstack11l111_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩἡ")]), None)
            step.update({
                bstack11l111_opy_ (u"ࠫ࡫࡯࡮ࡪࡵ࡫ࡩࡩࡥࡡࡵࠩἢ"): bstack1ll1l1ll11l_opy_,
                bstack11l111_opy_ (u"ࠬࡪࡵࡳࡣࡷ࡭ࡴࡴࠧἣ"): duration if duration else bstack1111l11llll_opy_(step[bstack11l111_opy_ (u"࠭ࡳࡵࡣࡵࡸࡪࡪ࡟ࡢࡶࠪἤ")], bstack1ll1l1ll11l_opy_),
                bstack11l111_opy_ (u"ࠧࡳࡧࡶࡹࡱࡺࠧἥ"): result.result,
                bstack11l111_opy_ (u"ࠨࡨࡤ࡭ࡱࡻࡲࡦࠩἦ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack111111lll1l_opy_):
        if self.meta.get(bstack11l111_opy_ (u"ࠩࡶࡸࡪࡶࡳࠨἧ")):
            self.meta[bstack11l111_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩἨ")].append(bstack111111lll1l_opy_)
        else:
            self.meta[bstack11l111_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪἩ")] = [ bstack111111lll1l_opy_ ]
    def bstack111111ll1ll_opy_(self):
        return {
            bstack11l111_opy_ (u"ࠬࡻࡵࡪࡦࠪἪ"): self.bstack1l1l1ll1_opy_(),
            **self.bstack111111l11l1_opy_(),
            **self.bstack111111ll11l_opy_(),
            **self.bstack111111llll1_opy_()
        }
    def bstack111111l1l1l_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack11l111_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫἫ"): self.bstack1ll1l1ll11l_opy_,
            bstack11l111_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࡡ࡬ࡲࡤࡳࡳࠨἬ"): self.duration,
            bstack11l111_opy_ (u"ࠨࡴࡨࡷࡺࡲࡴࠨἭ"): self.result.result
        }
        if data[bstack11l111_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩἮ")] == bstack11l111_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪἯ"):
            data[bstack11l111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡷࡵࡩࡤࡺࡹࡱࡧࠪἰ")] = self.result.bstack1111111lll_opy_()
            data[bstack11l111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡸࡶࡪ࠭ἱ")] = [{bstack11l111_opy_ (u"࠭ࡢࡢࡥ࡮ࡸࡷࡧࡣࡦࠩἲ"): self.result.bstack111l1ll1lll_opy_()}]
        return data
    def bstack111111l111l_opy_(self):
        return {
            bstack11l111_opy_ (u"ࠧࡶࡷ࡬ࡨࠬἳ"): self.bstack1l1l1ll1_opy_(),
            **self.bstack111111l11l1_opy_(),
            **self.bstack111111ll11l_opy_(),
            **self.bstack111111l1l1l_opy_(),
            **self.bstack111111llll1_opy_()
        }
    def bstack1l11llll_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack11l111_opy_ (u"ࠨࡕࡷࡥࡷࡺࡥࡥࠩἴ") in event:
            return self.bstack111111ll1ll_opy_()
        elif bstack11l111_opy_ (u"ࠩࡉ࡭ࡳ࡯ࡳࡩࡧࡧࠫἵ") in event:
            return self.bstack111111l111l_opy_()
    def event_key(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1ll1l1ll11l_opy_ = time if time else bstack11lllll1_opy_()
        self.duration = duration if duration else bstack1111l11llll_opy_(self.started_at, self.bstack1ll1l1ll11l_opy_)
        if result:
            self.result = result
class bstack1ll1lll1_opy_(bstack1l1l11ll_opy_):
    def __init__(self, hooks=[], bstack1ll11l11_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack1ll11l11_opy_ = bstack1ll11l11_opy_
        super().__init__(*args, **kwargs, bstack1ll111111l_opy_=bstack11l111_opy_ (u"ࠪࡸࡪࡹࡴࠨἶ"))
    @classmethod
    def bstack111111lll11_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack11l111_opy_ (u"ࠫ࡮ࡪࠧἷ"): id(step),
                bstack11l111_opy_ (u"ࠬࡺࡥࡹࡶࠪἸ"): step.name,
                bstack11l111_opy_ (u"࠭࡫ࡦࡻࡺࡳࡷࡪࠧἹ"): step.keyword,
            })
        return bstack1ll1lll1_opy_(
            **kwargs,
            meta={
                bstack11l111_opy_ (u"ࠧࡧࡧࡤࡸࡺࡸࡥࠨἺ"): {
                    bstack11l111_opy_ (u"ࠨࡰࡤࡱࡪ࠭Ἳ"): feature.name,
                    bstack11l111_opy_ (u"ࠩࡳࡥࡹ࡮ࠧἼ"): feature.filename,
                    bstack11l111_opy_ (u"ࠪࡨࡪࡹࡣࡳ࡫ࡳࡸ࡮ࡵ࡮ࠨἽ"): feature.description
                },
                bstack11l111_opy_ (u"ࠫࡸࡩࡥ࡯ࡣࡵ࡭ࡴ࠭Ἶ"): {
                    bstack11l111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪἿ"): scenario.name
                },
                bstack11l111_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬὀ"): steps,
                bstack11l111_opy_ (u"ࠧࡦࡺࡤࡱࡵࡲࡥࡴࠩὁ"): bstack11l111l11l1_opy_(test)
            }
        )
    def bstack111111l1111_opy_(self):
        return {
            bstack11l111_opy_ (u"ࠨࡪࡲࡳࡰࡹࠧὂ"): self.hooks
        }
    def bstack111111ll1l1_opy_(self):
        if self.bstack1ll11l11_opy_:
            return {
                bstack11l111_opy_ (u"ࠩ࡬ࡲࡹ࡫ࡧࡳࡣࡷ࡭ࡴࡴࡳࠨὃ"): self.bstack1ll11l11_opy_
            }
        return {}
    def bstack111111l111l_opy_(self):
        return {
            **super().bstack111111l111l_opy_(),
            **self.bstack111111l1111_opy_()
        }
    def bstack111111ll1ll_opy_(self):
        return {
            **super().bstack111111ll1ll_opy_(),
            **self.bstack111111ll1l1_opy_()
        }
    def event_key(self):
        return bstack11l111_opy_ (u"ࠪࡸࡪࡹࡴࡠࡴࡸࡲࠬὄ")
class bstack1lll1l11_opy_(bstack1l1l11ll_opy_):
    def __init__(self, hook_type, *args,bstack1ll11l11_opy_={}, **kwargs):
        self.hook_type = hook_type
        self.bstack1l1111ll11l_opy_ = None
        self.bstack1ll11l11_opy_ = bstack1ll11l11_opy_
        super().__init__(*args, **kwargs, bstack1ll111111l_opy_=bstack11l111_opy_ (u"ࠫ࡭ࡵ࡯࡬ࠩὅ"))
    def bstack1l1llll1_opy_(self):
        return self.hook_type
    def bstack111111lllll_opy_(self):
        return {
            bstack11l111_opy_ (u"ࠬ࡮࡯ࡰ࡭ࡢࡸࡾࡶࡥࠨ὆"): self.hook_type
        }
    def bstack111111l111l_opy_(self):
        return {
            **super().bstack111111l111l_opy_(),
            **self.bstack111111lllll_opy_()
        }
    def bstack111111ll1ll_opy_(self):
        return {
            **super().bstack111111ll1ll_opy_(),
            bstack11l111_opy_ (u"࠭ࡴࡦࡵࡷࡣࡷࡻ࡮ࡠ࡫ࡧࠫ὇"): self.bstack1l1111ll11l_opy_,
            **self.bstack111111lllll_opy_()
        }
    def event_key(self):
        return bstack11l111_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡸࡵ࡯ࠩὈ")
    def bstack111lll1l_opy_(self, bstack1l1111ll11l_opy_):
        self.bstack1l1111ll11l_opy_ = bstack1l1111ll11l_opy_